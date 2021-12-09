Module(
    body=[
        Import(
            names=[alias(name='pytz', asname=None)],
        ),
        ImportFrom(
            module='datetime',
            names=[
                alias(name='datetime', asname=None),
                alias(name='time', asname=None),
                alias(name='timedelta', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='unittest.mock',
            names=[alias(name='patch', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='fields', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='common', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.lunch.tests.common',
            names=[alias(name='TestsCommon', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestSupplier',
            bases=[Name(id='TestsCommon', ctx=Load())],
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
                                        args=[
                                            Name(id='TestSupplier', ctx=Load()),
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
                                    attr='monday_1am',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='datetime', ctx=Load()),
                                args=[
                                    Constant(value=2018, kind=None),
                                    Constant(value=10, kind=None),
                                    Constant(value=29, kind=None),
                                    Constant(value=1, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='monday_10am',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='datetime', ctx=Load()),
                                args=[
                                    Constant(value=2018, kind=None),
                                    Constant(value=10, kind=None),
                                    Constant(value=29, kind=None),
                                    Constant(value=10, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='monday_1pm',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='datetime', ctx=Load()),
                                args=[
                                    Constant(value=2018, kind=None),
                                    Constant(value=10, kind=None),
                                    Constant(value=29, kind=None),
                                    Constant(value=13, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='monday_8pm',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='datetime', ctx=Load()),
                                args=[
                                    Constant(value=2018, kind=None),
                                    Constant(value=10, kind=None),
                                    Constant(value=29, kind=None),
                                    Constant(value=20, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='saturday_3am',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='datetime', ctx=Load()),
                                args=[
                                    Constant(value=2018, kind=None),
                                    Constant(value=11, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='saturday_10am',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='datetime', ctx=Load()),
                                args=[
                                    Constant(value=2018, kind=None),
                                    Constant(value=11, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=10, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='saturday_1pm',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='datetime', ctx=Load()),
                                args=[
                                    Constant(value=2018, kind=None),
                                    Constant(value=11, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=13, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='saturday_8pm',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='datetime', ctx=Load()),
                                args=[
                                    Constant(value=2018, kind=None),
                                    Constant(value=11, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=20, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_send_email_cron',
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='supplier_kothai',
                                            ctx=Load(),
                                        ),
                                        attr='cron_id',
                                        ctx=Load(),
                                    ),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='supplier_kothai',
                                                        ctx=Load(),
                                                    ),
                                                    attr='cron_id',
                                                    ctx=Load(),
                                                ),
                                                attr='nextcall',
                                                ctx=Load(),
                                            ),
                                            attr='time',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='time', ctx=Load()),
                                        args=[
                                            Constant(value=15, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
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
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='supplier_kothai',
                                                ctx=Load(),
                                            ),
                                            attr='cron_id',
                                            ctx=Load(),
                                        ),
                                        attr='code',
                                        ctx=Load(),
                                    ),
                                    JoinedStr(
                                        values=[
                                            Constant(value="# This cron is dynamically controlled by Lunch Supplier.\n# Do NOT modify this cron, modify the related record instead.\nenv['lunch.supplier'].browse([", kind=None),
                                            FormattedValue(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='supplier_kothai',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='])._send_auto_email()', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='cron_id', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='supplier_kothai',
                                        ctx=Load(),
                                    ),
                                    attr='cron_id',
                                    ctx=Load(),
                                ),
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
                                        attr='supplier_kothai',
                                        ctx=Load(),
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ir.cron', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
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
                                                            Name(id='cron_id', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='common', ctx=Load()),
                                attr='users',
                                ctx=Load(),
                            ),
                            args=[Constant(value='cle-lunch-manager', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_compute_available_today',
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
                            targets=[Name(id='tests', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='monday_1am',
                                                ctx=Load(),
                                            ),
                                            Constant(value=True, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='monday_10am',
                                                ctx=Load(),
                                            ),
                                            Constant(value=True, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='monday_1pm',
                                                ctx=Load(),
                                            ),
                                            Constant(value=True, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='monday_8pm',
                                                ctx=Load(),
                                            ),
                                            Constant(value=True, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='saturday_3am',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='saturday_10am',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='saturday_1pm',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='saturday_8pm',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='value', ctx=Store()),
                                    Name(id='result', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='tests', ctx=Load()),
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='patch', ctx=Load()),
                                                    attr='object',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Datetime',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='now', kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='return_value',
                                                        value=Name(id='value', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            optional_vars=Name(id='_', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assert(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='supplier_pizza_inn',
                                                        ctx=Load(),
                                                    ),
                                                    attr='available_today',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Name(id='result', ctx=Load())],
                                            ),
                                            msg=BinOp(
                                                left=Constant(value='supplier pizza inn should %s considered available on %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        IfExp(
                                                            test=Name(id='result', ctx=Load()),
                                                            body=Constant(value='be', kind=None),
                                                            orelse=Constant(value='not be', kind=None),
                                                        ),
                                                        Name(id='value', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                    ],
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
                                                slice=Constant(value='lunch.supplier', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='invalidate_cache',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[Constant(value='available_today', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='supplier_pizza_inn',
                                                            ctx=Load(),
                                                        ),
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='common', ctx=Load()),
                                attr='users',
                                ctx=Load(),
                            ),
                            args=[Constant(value='cle-lunch-manager', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_search_available_today',
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
                            value=Constant(value='\n            This test checks that _search_available_today returns a valid domain\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                    attr='tz',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='Europe/Brussels', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Supplier', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='lunch.supplier', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tests', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='monday_1am',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1.0, kind=None),
                                            Constant(value='mon', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='monday_10am',
                                                ctx=Load(),
                                            ),
                                            Constant(value=10.0, kind=None),
                                            Constant(value='mon', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='monday_1pm',
                                                ctx=Load(),
                                            ),
                                            Constant(value=13.0, kind=None),
                                            Constant(value='mon', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='monday_8pm',
                                                ctx=Load(),
                                            ),
                                            Constant(value=20.0, kind=None),
                                            Constant(value='mon', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='saturday_3am',
                                                ctx=Load(),
                                            ),
                                            Constant(value=3.0, kind=None),
                                            Constant(value='sat', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='saturday_10am',
                                                ctx=Load(),
                                            ),
                                            Constant(value=10.0, kind=None),
                                            Constant(value='sat', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='saturday_1pm',
                                                ctx=Load(),
                                            ),
                                            Constant(value=13.0, kind=None),
                                            Constant(value='sat', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='saturday_8pm',
                                                ctx=Load(),
                                            ),
                                            Constant(value=20.0, kind=None),
                                            Constant(value='sat', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='Supplier', ctx=Load()),
                                        attr='_search_available_today',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='>', kind=None),
                                        Constant(value=7, kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[List(elts=[], ctx=Load())],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='Supplier', ctx=Load()),
                                        attr='_search_available_today',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='>', kind=None),
                                        Constant(value=True, kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[List(elts=[], ctx=Load())],
                            ),
                            msg=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='value', ctx=Store()),
                                    Name(id='rvalue', ctx=Store()),
                                    Name(id='dayname', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='tests', ctx=Load()),
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='patch', ctx=Load()),
                                                    attr='object',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Datetime',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='now', kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='return_value',
                                                        value=Name(id='value', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            optional_vars=Name(id='_', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assert(
                                            test=Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='Supplier', ctx=Load()),
                                                        attr='_search_available_today',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='=', kind=None),
                                                        Constant(value=True, kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    List(
                                                        elts=[
                                                            Constant(value='&', kind=None),
                                                            Constant(value='|', kind=None),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='recurrency_end_date', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value=False, kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='recurrency_end_date', kind=None),
                                                                    Constant(value='>', kind=None),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='value', ctx=Load()),
                                                                                    attr='replace',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[],
                                                                                keywords=[
                                                                                    keyword(
                                                                                        arg='tzinfo',
                                                                                        value=Attribute(
                                                                                            value=Name(id='pytz', ctx=Load()),
                                                                                            attr='UTC',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            attr='astimezone',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='pytz', ctx=Load()),
                                                                                    attr='timezone',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='env',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='user',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='tz',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Name(id='dayname', ctx=Load()),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value=True, kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            msg=BinOp(
                                                left=Constant(value='Wrong domain generated for values (%s, %s)', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='value', ctx=Load()),
                                                        Name(id='rvalue', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='patch', ctx=Load()),
                                            attr='object',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Datetime',
                                                ctx=Load(),
                                            ),
                                            Constant(value='now', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='return_value',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='monday_10am',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    optional_vars=Name(id='_', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assert(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='supplier_pizza_inn',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='Supplier', ctx=Load()),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='available_today', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value=True, kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    msg=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='common', ctx=Load()),
                                attr='users',
                                ctx=Load(),
                            ),
                            args=[Constant(value='cle-lunch-manager', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_auto_email_send',
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
                                        func=Attribute(
                                            value=Name(id='patch', ctx=Load()),
                                            attr='object',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Datetime',
                                                ctx=Load(),
                                            ),
                                            Constant(value='now', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='return_value',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='monday_1pm',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    optional_vars=Name(id='_', ctx=Store()),
                                ),
                            ],
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='patch', ctx=Load()),
                                                    attr='object',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='today', kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='return_value',
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='monday_1pm',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='date',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            optional_vars=Name(id='_', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        With(
                                            items=[
                                                withitem(
                                                    context_expr=Call(
                                                        func=Attribute(
                                                            value=Name(id='patch', ctx=Load()),
                                                            attr='object',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='Date',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='context_today', kind=None),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='return_value',
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='monday_1pm',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='date',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    optional_vars=Name(id='_', ctx=Store()),
                                                ),
                                            ],
                                            body=[
                                                Assign(
                                                    targets=[Name(id='line', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='lunch.order', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='date', kind=None),
                                                                    Constant(value='supplier_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_pizza',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='monday_1pm',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='date',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='supplier_pizza_inn',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
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
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='action_order',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assert(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='state',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='ordered', kind=None)],
                                                    ),
                                                    msg=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='supplier_pizza_inn',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_send_auto_email',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assert(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='state',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='confirmed', kind=None)],
                                                    ),
                                                    msg=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='line', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='lunch.order', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='topping_ids_1', kind=None),
                                                                    Constant(value='date', kind=None),
                                                                    Constant(value='supplier_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_pizza',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=6, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='topping_olives',
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
                                                                        ctx=Load(),
                                                                    ),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='monday_1pm',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='date',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='supplier_pizza_inn',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
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
                                                    targets=[Name(id='line2', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='lunch.order', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='date', kind=None),
                                                                    Constant(value='supplier_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_sandwich_tuna',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='monday_1pm',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='date',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='supplier_coin_gourmand',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
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
                                                            value=BinOp(
                                                                left=Name(id='line', ctx=Load()),
                                                                op=BitOr(),
                                                                right=Name(id='line2', ctx=Load()),
                                                            ),
                                                            attr='action_order',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assert(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='state',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='ordered', kind=None)],
                                                    ),
                                                    msg=None,
                                                ),
                                                Assert(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='line2', ctx=Load()),
                                                            attr='state',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='ordered', kind=None)],
                                                    ),
                                                    msg=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='supplier_pizza_inn',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_send_auto_email',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assert(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='state',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='confirmed', kind=None)],
                                                    ),
                                                    msg=None,
                                                ),
                                                Assert(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='line2', ctx=Load()),
                                                            attr='state',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='ordered', kind=None)],
                                                    ),
                                                    msg=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='line_1', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='lunch.order', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='quantity', kind=None),
                                                                    Constant(value='date', kind=None),
                                                                    Constant(value='supplier_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_pizza',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=2, kind=None),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='monday_1pm',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='date',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_pizza',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
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
                                                    targets=[Name(id='line_2', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='lunch.order', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='topping_ids_1', kind=None),
                                                                    Constant(value='date', kind=None),
                                                                    Constant(value='supplier_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_pizza',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=6, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='topping_olives',
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
                                                                        ctx=Load(),
                                                                    ),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='monday_1pm',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='date',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_pizza',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
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
                                                    targets=[Name(id='line_3', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='lunch.order', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='quantity', kind=None),
                                                                    Constant(value='date', kind=None),
                                                                    Constant(value='supplier_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_sandwich_tuna',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=2, kind=None),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='monday_1pm',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='date',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='supplier_coin_gourmand',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
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
                                                            value=BinOp(
                                                                left=BinOp(
                                                                    left=Name(id='line_1', ctx=Load()),
                                                                    op=BitOr(),
                                                                    right=Name(id='line_2', ctx=Load()),
                                                                ),
                                                                op=BitOr(),
                                                                right=Name(id='line_3', ctx=Load()),
                                                            ),
                                                            attr='action_order',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assert(
                                                    test=Call(
                                                        func=Name(id='all', ctx=Load()),
                                                        args=[
                                                            GeneratorExp(
                                                                elt=Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='state',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[Constant(value='ordered', kind=None)],
                                                                ),
                                                                generators=[
                                                                    comprehension(
                                                                        target=Name(id='line', ctx=Store()),
                                                                        iter=List(
                                                                            elts=[
                                                                                Name(id='line_1', ctx=Load()),
                                                                                Name(id='line_2', ctx=Load()),
                                                                                Name(id='line_3', ctx=Load()),
                                                                            ],
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
                                                    msg=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='supplier_pizza_inn',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_send_auto_email',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='common', ctx=Load()),
                                attr='users',
                                ctx=Load(),
                            ),
                            args=[Constant(value='cle-lunch-manager', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_cron_sync_create',
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
                            targets=[Name(id='cron_ny', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='supplier_kothai',
                                    ctx=Load(),
                                ),
                                attr='cron_id',
                                ctx=Load(),
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
                                args=[
                                    Attribute(
                                        value=Name(id='cron_ny', ctx=Load()),
                                        attr='active',
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
                                    Attribute(
                                        value=Name(id='cron_ny', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Lunch: send automatic email to Kothai', kind=None),
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
                                    ListComp(
                                        elt=Name(id='line', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='line', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='cron_ny', ctx=Load()),
                                                            attr='code',
                                                            ctx=Load(),
                                                        ),
                                                        attr='splitlines',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ifs=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='lstrip',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                attr='startswith',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='#', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    List(
                                        elts=[
                                            BinOp(
                                                left=Constant(value="env['lunch.supplier'].browse([%i])._send_auto_email()", kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='supplier_kothai',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
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
                                    Attribute(
                                        value=Name(id='cron_ny', ctx=Load()),
                                        attr='nextcall',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2021, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=29, kind=None),
                                            Constant(value=15, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='common', ctx=Load()),
                                attr='users',
                                ctx=Load(),
                            ),
                            args=[Constant(value='cle-lunch-manager', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_cron_sync_active',
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
                            targets=[Name(id='cron_ny', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='supplier_kothai',
                                    ctx=Load(),
                                ),
                                attr='cron_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='supplier_kothai',
                                        ctx=Load(),
                                    ),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='cron_ny', ctx=Load()),
                                        attr='active',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='supplier_kothai',
                                        ctx=Load(),
                                    ),
                                    attr='active',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='cron_ny', ctx=Load()),
                                        attr='active',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='supplier_kothai',
                                        ctx=Load(),
                                    ),
                                    attr='send_by',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='phone', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='cron_ny', ctx=Load()),
                                        attr='active',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='supplier_kothai',
                                        ctx=Load(),
                                    ),
                                    attr='send_by',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='mail', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='cron_ny', ctx=Load()),
                                        attr='active',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='common', ctx=Load()),
                                attr='users',
                                ctx=Load(),
                            ),
                            args=[Constant(value='cle-lunch-manager', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_cron_sync_nextcall',
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
                            targets=[Name(id='cron_ny', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='supplier_kothai',
                                    ctx=Load(),
                                ),
                                attr='cron_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='old_nextcall', ctx=Store())],
                            value=Attribute(
                                value=Name(id='cron_ny', ctx=Load()),
                                attr='nextcall',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='supplier_kothai',
                                    ctx=Load(),
                                ),
                                attr='automatic_email_time',
                                ctx=Store(),
                            ),
                            op=Sub(),
                            value=Constant(value=5, kind=None),
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
                                        value=Name(id='cron_ny', ctx=Load()),
                                        attr='nextcall',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='old_nextcall', ctx=Load()),
                                            op=Sub(),
                                            right=Call(
                                                func=Name(id='timedelta', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='hours',
                                                        value=Constant(value=5, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id='timedelta', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='days',
                                                    value=Constant(value=1, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cron_ny', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='lastcall',
                                    ctx=Store(),
                                ),
                            ],
                            value=BinOp(
                                left=Name(id='old_nextcall', ctx=Load()),
                                op=Sub(),
                                right=Call(
                                    func=Name(id='timedelta', ctx=Load()),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='hours',
                                            value=Constant(value=5, kind=None),
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='cron_ny', ctx=Load()),
                                        attr='sudo',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                attr='nextcall',
                                ctx=Store(),
                            ),
                            op=Add(),
                            value=Call(
                                func=Name(id='timedelta', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='days',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        AugAssign(
                            target=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='supplier_kothai',
                                    ctx=Load(),
                                ),
                                attr='automatic_email_time',
                                ctx=Store(),
                            ),
                            op=Add(),
                            value=Constant(value=7, kind=None),
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
                                        value=Name(id='cron_ny', ctx=Load()),
                                        attr='nextcall',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Name(id='old_nextcall', ctx=Load()),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id='timedelta', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='days',
                                                    value=Constant(value=1, kind=None),
                                                ),
                                                keyword(
                                                    arg='hours',
                                                    value=Constant(value=2, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        AugAssign(
                            target=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='supplier_kothai',
                                    ctx=Load(),
                                ),
                                attr='automatic_email_time',
                                ctx=Store(),
                            ),
                            op=Sub(),
                            value=Constant(value=1, kind=None),
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
                                        value=Name(id='cron_ny', ctx=Load()),
                                        attr='nextcall',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Name(id='old_nextcall', ctx=Load()),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id='timedelta', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='days',
                                                    value=Constant(value=1, kind=None),
                                                ),
                                                keyword(
                                                    arg='hours',
                                                    value=Constant(value=1, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='common', ctx=Load()),
                                attr='users',
                                ctx=Load(),
                            ),
                            args=[Constant(value='cle-lunch-manager', kind=None)],
                            keywords=[],
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
