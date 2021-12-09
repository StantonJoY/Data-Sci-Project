Module(
    body=[
        ImportFrom(
            module='datetime',
            names=[alias(name='date', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='Command', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[
                alias(name='users', asname=None),
                alias(name='tagged', asname=None),
                alias(name='TransactionCase', asname=None),
                alias(name='warmup', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.misc',
            names=[
                alias(name='DEFAULT_SERVER_DATE_FORMAT', asname=None),
                alias(name='DEFAULT_SERVER_DATETIME_FORMAT', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='TestDiscussFullPerformance',
            bases=[Name(id='TransactionCase', ctx=Load())],
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
                                    attr='users',
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
                                        slice=Constant(value='res.users', kind=None),
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
                                                    Constant(value='email', kind=None),
                                                    Constant(value='groups_id', kind=None),
                                                    Constant(value='login', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='notification_type', kind=None),
                                                    Constant(value='signature', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='e.e@example.com', kind=None),
                                                    List(
                                                        elts=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='link',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='env',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='ref',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Constant(value='base.group_user', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='emp', kind=None),
                                                    Constant(value='Ernest Employee', kind=None),
                                                    Constant(value='inbox', kind=None),
                                                    Constant(value='--\nErnest', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='login', kind=None),
                                                    Constant(value='email', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='test1', kind=None),
                                                    Constant(value='test1', kind=None),
                                                    Constant(value='test1@example.com', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='login', kind=None),
                                                    Constant(value='email', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='test2', kind=None),
                                                    Constant(value='test2', kind=None),
                                                    Constant(value='test2@example.com', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='login', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='test3', kind=None),
                                                    Constant(value='test3', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='login', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='test4', kind=None),
                                                    Constant(value='test4', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='login', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='test5', kind=None),
                                                    Constant(value='test5', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='login', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='test6', kind=None),
                                                    Constant(value='test6', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='login', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='test7', kind=None),
                                                    Constant(value='test7', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='login', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='test8', kind=None),
                                                    Constant(value='test8', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='login', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='test9', kind=None),
                                                    Constant(value='test9', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='login', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='test10', kind=None),
                                                    Constant(value='test10', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='login', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='test11', kind=None),
                                                    Constant(value='test11', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='login', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='test12', kind=None),
                                                    Constant(value='test12', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='login', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='test13', kind=None),
                                                    Constant(value='test13', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='login', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='test14', kind=None),
                                                    Constant(value='test14', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='login', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='test15', kind=None),
                                                    Constant(value='test15', kind=None),
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
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='employees',
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
                                        slice=Constant(value='hr.employee', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Dict(
                                            keys=[Constant(value='user_id', kind=None)],
                                            values=[
                                                Attribute(
                                                    value=Name(id='user', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='user', ctx=Store()),
                                                iter=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='users',
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='leave_type',
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
                                        slice=Constant(value='hr.leave.type', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='requires_allocation', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='time_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='no', kind=None),
                                            Constant(value='Legal Leaves', kind=None),
                                            Constant(value='leave', kind=None),
                                        ],
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
                                    attr='leaves',
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
                                        slice=Constant(value='hr.leave', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='date_from', kind=None),
                                                Constant(value='date_to', kind=None),
                                                Constant(value='employee_id', kind=None),
                                                Constant(value='holiday_status_id', kind=None),
                                            ],
                                            values=[
                                                BinOp(
                                                    left=Call(
                                                        func=Attribute(
                                                            value=Name(id='date', ctx=Load()),
                                                            attr='today',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    op=Add(),
                                                    right=Call(
                                                        func=Name(id='relativedelta', ctx=Load()),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='days',
                                                                value=UnaryOp(
                                                                    op=USub(),
                                                                    operand=Constant(value=2, kind=None),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                                BinOp(
                                                    left=Call(
                                                        func=Attribute(
                                                            value=Name(id='date', ctx=Load()),
                                                            attr='today',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    op=Add(),
                                                    right=Call(
                                                        func=Name(id='relativedelta', ctx=Load()),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='days',
                                                                value=Constant(value=2, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                                Attribute(
                                                    value=Name(id='employee', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='leave_type',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='employee', ctx=Store()),
                                                iter=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='employees',
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_init_messaging',
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
                            value=Constant(value='Test performance of `_init_messaging`.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='channel_general', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='mail.channel_all_employees', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='mail.channel', kind=None),
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
                                                            Constant(value='!=', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_general', ctx=Load()),
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
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='user_root', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.user_root', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='channel_channel_public_1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.channel', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='mail.channel', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='channel_create',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='name',
                                                    value=Constant(value='public 1', kind=None),
                                                ),
                                                keyword(
                                                    arg='privacy',
                                                    value=Constant(value='public', kind=None),
                                                ),
                                            ],
                                        ),
                                        slice=Constant(value='id', kind=None),
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
                                    value=Name(id='channel_channel_public_1', ctx=Load()),
                                    attr='add_members',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=BinOp(
                                                left=BinOp(
                                                    left=BinOp(
                                                        left=BinOp(
                                                            left=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='users',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            op=Add(),
                                                            right=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='users',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=2, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        op=Add(),
                                                        right=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='users',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=3, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    op=Add(),
                                                    right=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='users',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=4, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                op=Add(),
                                                right=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='users',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=8, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='channel_channel_public_2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.channel', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='mail.channel', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='channel_create',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='name',
                                                    value=Constant(value='public 2', kind=None),
                                                ),
                                                keyword(
                                                    arg='privacy',
                                                    value=Constant(value='public', kind=None),
                                                ),
                                            ],
                                        ),
                                        slice=Constant(value='id', kind=None),
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
                                    value=Name(id='channel_channel_public_2', ctx=Load()),
                                    attr='add_members',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=BinOp(
                                                left=BinOp(
                                                    left=BinOp(
                                                        left=BinOp(
                                                            left=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='users',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            op=Add(),
                                                            right=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='users',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=2, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        op=Add(),
                                                        right=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='users',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=4, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    op=Add(),
                                                    right=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='users',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=7, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                op=Add(),
                                                right=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='users',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=9, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='channel_channel_group_1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.channel', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='mail.channel', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='channel_create',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='name',
                                                    value=Constant(value='group 1', kind=None),
                                                ),
                                                keyword(
                                                    arg='privacy',
                                                    value=Constant(value='groups', kind=None),
                                                ),
                                            ],
                                        ),
                                        slice=Constant(value='id', kind=None),
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
                                    value=Name(id='channel_channel_group_1', ctx=Load()),
                                    attr='add_members',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=BinOp(
                                                left=BinOp(
                                                    left=BinOp(
                                                        left=BinOp(
                                                            left=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='users',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            op=Add(),
                                                            right=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='users',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=2, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        op=Add(),
                                                        right=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='users',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=3, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    op=Add(),
                                                    right=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='users',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=6, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                op=Add(),
                                                right=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='users',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=12, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='channel_channel_group_2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.channel', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='mail.channel', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='channel_create',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='name',
                                                    value=Constant(value='group 2', kind=None),
                                                ),
                                                keyword(
                                                    arg='privacy',
                                                    value=Constant(value='groups', kind=None),
                                                ),
                                            ],
                                        ),
                                        slice=Constant(value='id', kind=None),
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
                                    value=Name(id='channel_channel_group_2', ctx=Load()),
                                    attr='add_members',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=BinOp(
                                                left=BinOp(
                                                    left=BinOp(
                                                        left=BinOp(
                                                            left=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='users',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            op=Add(),
                                                            right=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='users',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=2, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        op=Add(),
                                                        right=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='users',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=6, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    op=Add(),
                                                    right=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='users',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=7, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                op=Add(),
                                                right=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='users',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=13, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='channel_channel_private_1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.channel', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='mail.channel', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='channel_create',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='name',
                                                    value=Constant(value='private 1', kind=None),
                                                ),
                                                keyword(
                                                    arg='privacy',
                                                    value=Constant(value='private', kind=None),
                                                ),
                                            ],
                                        ),
                                        slice=Constant(value='id', kind=None),
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
                                    value=Name(id='channel_channel_private_1', ctx=Load()),
                                    attr='add_members',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=BinOp(
                                                left=BinOp(
                                                    left=BinOp(
                                                        left=BinOp(
                                                            left=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='users',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            op=Add(),
                                                            right=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='users',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=2, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        op=Add(),
                                                        right=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='users',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=3, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    op=Add(),
                                                    right=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='users',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=5, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                op=Add(),
                                                right=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='users',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=10, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='channel_channel_private_2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.channel', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='mail.channel', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='channel_create',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='name',
                                                    value=Constant(value='private 2', kind=None),
                                                ),
                                                keyword(
                                                    arg='privacy',
                                                    value=Constant(value='private', kind=None),
                                                ),
                                            ],
                                        ),
                                        slice=Constant(value='id', kind=None),
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
                                    value=Name(id='channel_channel_private_2', ctx=Load()),
                                    attr='add_members',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=BinOp(
                                                left=BinOp(
                                                    left=BinOp(
                                                        left=BinOp(
                                                            left=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='users',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            op=Add(),
                                                            right=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='users',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=2, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        op=Add(),
                                                        right=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='users',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=5, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    op=Add(),
                                                    right=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='users',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=7, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                op=Add(),
                                                right=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='users',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=11, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='channel_chat_1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.channel', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='mail.channel', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='channel_get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=BinOp(
                                                            left=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='users',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            op=Add(),
                                                            right=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='users',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=14, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Constant(value='id', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='channel_chat_2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.channel', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='mail.channel', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='channel_get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=BinOp(
                                                            left=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='users',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            op=Add(),
                                                            right=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='users',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=15, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Constant(value='id', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='channel_chat_3', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.channel', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='mail.channel', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='channel_get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=BinOp(
                                                            left=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='users',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            op=Add(),
                                                            right=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='users',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=2, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Constant(value='id', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='channel_chat_4', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.channel', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='mail.channel', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='channel_get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=BinOp(
                                                            left=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='users',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            op=Add(),
                                                            right=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='users',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=3, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Constant(value='id', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='channel_group_1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.channel', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='mail.channel', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='create_group',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=BinOp(
                                                            left=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='users',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            op=Add(),
                                                            right=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='users',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=12, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Constant(value='id', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='im_livechat_channel', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='im_livechat.channel', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='user_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='support', kind=None),
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='link',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
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
                                                        keywords=[],
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
                                    attr='im_status',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='online', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='channel_livechat_1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.channel', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='im_livechat_channel', ctx=Load()),
                                                attr='_open_livechat_mail_channel',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='anonymous_name',
                                                    value=Constant(value='anon 1', kind=None),
                                                ),
                                                keyword(
                                                    arg='previous_operator_id',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='users',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                keyword(
                                                    arg='user_id',
                                                    value=Attribute(
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
                                                ),
                                                keyword(
                                                    arg='country_id',
                                                    value=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='ref',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='base.in', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        slice=Constant(value='id', kind=None),
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
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='channel_livechat_1', ctx=Load()),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='users',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='message_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='body',
                                        value=Constant(value='test', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='channel_livechat_2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.channel', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='im_livechat_channel', ctx=Load()),
                                                        attr='with_user',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='ref',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='base.public_user', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                attr='_open_livechat_mail_channel',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='anonymous_name',
                                                    value=Constant(value='anon 2', kind=None),
                                                ),
                                                keyword(
                                                    arg='previous_operator_id',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='users',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                keyword(
                                                    arg='country_id',
                                                    value=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='ref',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='base.be', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        slice=Constant(value='id', kind=None),
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
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='channel_livechat_2', ctx=Load()),
                                                    attr='with_user',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ref',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='base.public_user', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='message_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='body',
                                        value=Constant(value='test', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[
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
                                    attr='notification_type',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='inbox', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='message', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='channel_channel_public_1', ctx=Load()),
                                    attr='message_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='body',
                                        value=Constant(value='test', kind=None),
                                    ),
                                    keyword(
                                        arg='message_type',
                                        value=Constant(value='comment', kind=None),
                                    ),
                                    keyword(
                                        arg='author_id',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='users',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=2, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='partner_ids',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='users',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            attr='ids',
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
                                    value=Name(id='message', ctx=Load()),
                                    attr='toggle_message_starred',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='name',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='YourCompany', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='maxDiff',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='users',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='users',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='invalidate_cache',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=90, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='init_messaging', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='users',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_user',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='users',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='_init_messaging',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='init_messaging', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='needaction_inbox_counter', kind=None),
                                            Constant(value='starred_counter', kind=None),
                                            Constant(value='channels', kind=None),
                                            Constant(value='companyName', kind=None),
                                            Constant(value='mail_failures', kind=None),
                                            Constant(value='shortcodes', kind=None),
                                            Constant(value='menu_id', kind=None),
                                            Constant(value='partner_root', kind=None),
                                            Constant(value='public_partners', kind=None),
                                            Constant(value='currentGuest', kind=None),
                                            Constant(value='current_partner', kind=None),
                                            Constant(value='current_user_id', kind=None),
                                            Constant(value='current_user_settings', kind=None),
                                        ],
                                        values=[
                                            Constant(value=1, kind=None),
                                            Constant(value=1, kind=None),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='avatarCacheKey', kind=None),
                                                            Constant(value='channel_type', kind=None),
                                                            Constant(value='create_uid', kind=None),
                                                            Constant(value='custom_channel_name', kind=None),
                                                            Constant(value='defaultDisplayMode', kind=None),
                                                            Constant(value='description', kind=None),
                                                            Constant(value='group_based_subscription', kind=None),
                                                            Constant(value='id', kind=None),
                                                            Constant(value='invitedGuests', kind=None),
                                                            Constant(value='invitedPartners', kind=None),
                                                            Constant(value='is_minimized', kind=None),
                                                            Constant(value='is_pinned', kind=None),
                                                            Constant(value='last_interest_dt', kind=None),
                                                            Constant(value='last_message_id', kind=None),
                                                            Constant(value='memberCount', kind=None),
                                                            Constant(value='message_needaction_counter', kind=None),
                                                            Constant(value='message_unread_counter', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='public', kind=None),
                                                            Constant(value='rtcSessions', kind=None),
                                                            Constant(value='seen_message_id', kind=None),
                                                            Constant(value='state', kind=None),
                                                            Constant(value='uuid', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='channel_general', ctx=Load()),
                                                                    attr='_get_avatar_cache_key',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            Constant(value='channel', kind=None),
                                                            Attribute(
                                                                value=Name(id='user_root', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Constant(value='General announcements for all employees.', kind=None),
                                                            Constant(value=True, kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_general', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
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
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=True, kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='channel_general', ctx=Load()),
                                                                                    attr='channel_last_seen_partner_ids',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='filtered',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Lambda(
                                                                                    args=arguments(
                                                                                        posonlyargs=[],
                                                                                        args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                                        vararg=None,
                                                                                        kwonlyargs=[],
                                                                                        kw_defaults=[],
                                                                                        kwarg=None,
                                                                                        defaults=[],
                                                                                    ),
                                                                                    body=Compare(
                                                                                        left=Attribute(
                                                                                            value=Name(id='p', ctx=Load()),
                                                                                            attr='partner_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[
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
                                                                                                attr='partner_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='last_interest_dt',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='strftime',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='DEFAULT_SERVER_DATETIME_FORMAT', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Name(id='next', ctx=Load()),
                                                                args=[
                                                                    GeneratorExp(
                                                                        elt=Subscript(
                                                                            value=Name(id='res', ctx=Load()),
                                                                            slice=Constant(value='message_id', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='res', ctx=Store()),
                                                                                iter=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='channel_general', ctx=Load()),
                                                                                        attr='_channel_last_message_ids',
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
                                                            Call(
                                                                func=Name(id='len', ctx=Load()),
                                                                args=[
                                                                    BinOp(
                                                                        left=Attribute(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='env',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='ref',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='base.group_user', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                            attr='users',
                                                                            ctx=Load(),
                                                                        ),
                                                                        op=BitOr(),
                                                                        right=Name(id='user_root', ctx=Load()),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=5, kind=None),
                                                            Constant(value='general', kind=None),
                                                            Constant(value='groups', kind=None),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value='open', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_general', ctx=Load()),
                                                                attr='uuid',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='avatarCacheKey', kind=None),
                                                            Constant(value='channel_type', kind=None),
                                                            Constant(value='create_uid', kind=None),
                                                            Constant(value='custom_channel_name', kind=None),
                                                            Constant(value='defaultDisplayMode', kind=None),
                                                            Constant(value='description', kind=None),
                                                            Constant(value='group_based_subscription', kind=None),
                                                            Constant(value='id', kind=None),
                                                            Constant(value='invitedGuests', kind=None),
                                                            Constant(value='invitedPartners', kind=None),
                                                            Constant(value='is_minimized', kind=None),
                                                            Constant(value='is_pinned', kind=None),
                                                            Constant(value='last_interest_dt', kind=None),
                                                            Constant(value='last_message_id', kind=None),
                                                            Constant(value='message_needaction_counter', kind=None),
                                                            Constant(value='memberCount', kind=None),
                                                            Constant(value='message_unread_counter', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='public', kind=None),
                                                            Constant(value='rtcSessions', kind=None),
                                                            Constant(value='seen_message_id', kind=None),
                                                            Constant(value='state', kind=None),
                                                            Constant(value='uuid', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='channel_channel_public_1', ctx=Load()),
                                                                    attr='_get_avatar_cache_key',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            Constant(value='channel', kind=None),
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
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_channel_public_1', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
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
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=True, kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='channel_channel_public_1', ctx=Load()),
                                                                                    attr='channel_last_seen_partner_ids',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='filtered',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Lambda(
                                                                                    args=arguments(
                                                                                        posonlyargs=[],
                                                                                        args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                                        vararg=None,
                                                                                        kwonlyargs=[],
                                                                                        kw_defaults=[],
                                                                                        kwarg=None,
                                                                                        defaults=[],
                                                                                    ),
                                                                                    body=Compare(
                                                                                        left=Attribute(
                                                                                            value=Name(id='p', ctx=Load()),
                                                                                            attr='partner_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[
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
                                                                                                attr='partner_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='last_interest_dt',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='strftime',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='DEFAULT_SERVER_DATETIME_FORMAT', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Name(id='next', ctx=Load()),
                                                                args=[
                                                                    GeneratorExp(
                                                                        elt=Subscript(
                                                                            value=Name(id='res', ctx=Load()),
                                                                            slice=Constant(value='message_id', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='res', ctx=Store()),
                                                                                iter=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='channel_channel_public_1', ctx=Load()),
                                                                                        attr='_channel_last_message_ids',
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
                                                            Constant(value=1, kind=None),
                                                            Constant(value=5, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='public 1', kind=None),
                                                            Constant(value='public', kind=None),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Name(id='next', ctx=Load()),
                                                                args=[
                                                                    GeneratorExp(
                                                                        elt=Subscript(
                                                                            value=Name(id='res', ctx=Load()),
                                                                            slice=Constant(value='message_id', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='res', ctx=Store()),
                                                                                iter=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='channel_channel_public_1', ctx=Load()),
                                                                                        attr='_channel_last_message_ids',
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
                                                            Constant(value='open', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_channel_public_1', ctx=Load()),
                                                                attr='uuid',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='avatarCacheKey', kind=None),
                                                            Constant(value='channel_type', kind=None),
                                                            Constant(value='create_uid', kind=None),
                                                            Constant(value='custom_channel_name', kind=None),
                                                            Constant(value='defaultDisplayMode', kind=None),
                                                            Constant(value='description', kind=None),
                                                            Constant(value='group_based_subscription', kind=None),
                                                            Constant(value='id', kind=None),
                                                            Constant(value='invitedGuests', kind=None),
                                                            Constant(value='invitedPartners', kind=None),
                                                            Constant(value='is_minimized', kind=None),
                                                            Constant(value='is_pinned', kind=None),
                                                            Constant(value='last_interest_dt', kind=None),
                                                            Constant(value='last_message_id', kind=None),
                                                            Constant(value='memberCount', kind=None),
                                                            Constant(value='message_needaction_counter', kind=None),
                                                            Constant(value='message_unread_counter', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='public', kind=None),
                                                            Constant(value='rtcSessions', kind=None),
                                                            Constant(value='seen_message_id', kind=None),
                                                            Constant(value='state', kind=None),
                                                            Constant(value='uuid', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='channel_channel_public_2', ctx=Load()),
                                                                    attr='_get_avatar_cache_key',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            Constant(value='channel', kind=None),
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
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_channel_public_2', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
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
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=True, kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='channel_channel_public_2', ctx=Load()),
                                                                                    attr='channel_last_seen_partner_ids',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='filtered',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Lambda(
                                                                                    args=arguments(
                                                                                        posonlyargs=[],
                                                                                        args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                                        vararg=None,
                                                                                        kwonlyargs=[],
                                                                                        kw_defaults=[],
                                                                                        kwarg=None,
                                                                                        defaults=[],
                                                                                    ),
                                                                                    body=Compare(
                                                                                        left=Attribute(
                                                                                            value=Name(id='p', ctx=Load()),
                                                                                            attr='partner_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[
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
                                                                                                attr='partner_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='last_interest_dt',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='strftime',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='DEFAULT_SERVER_DATETIME_FORMAT', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Name(id='next', ctx=Load()),
                                                                args=[
                                                                    GeneratorExp(
                                                                        elt=Subscript(
                                                                            value=Name(id='res', ctx=Load()),
                                                                            slice=Constant(value='message_id', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='res', ctx=Store()),
                                                                                iter=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='channel_channel_public_2', ctx=Load()),
                                                                                        attr='_channel_last_message_ids',
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
                                                            Constant(value=5, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='public 2', kind=None),
                                                            Constant(value='public', kind=None),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Name(id='next', ctx=Load()),
                                                                args=[
                                                                    GeneratorExp(
                                                                        elt=Subscript(
                                                                            value=Name(id='res', ctx=Load()),
                                                                            slice=Constant(value='message_id', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='res', ctx=Store()),
                                                                                iter=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='channel_channel_public_2', ctx=Load()),
                                                                                        attr='_channel_last_message_ids',
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
                                                            Constant(value='open', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_channel_public_2', ctx=Load()),
                                                                attr='uuid',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='avatarCacheKey', kind=None),
                                                            Constant(value='channel_type', kind=None),
                                                            Constant(value='create_uid', kind=None),
                                                            Constant(value='custom_channel_name', kind=None),
                                                            Constant(value='defaultDisplayMode', kind=None),
                                                            Constant(value='description', kind=None),
                                                            Constant(value='group_based_subscription', kind=None),
                                                            Constant(value='id', kind=None),
                                                            Constant(value='invitedGuests', kind=None),
                                                            Constant(value='invitedPartners', kind=None),
                                                            Constant(value='is_minimized', kind=None),
                                                            Constant(value='is_pinned', kind=None),
                                                            Constant(value='last_interest_dt', kind=None),
                                                            Constant(value='last_message_id', kind=None),
                                                            Constant(value='memberCount', kind=None),
                                                            Constant(value='message_needaction_counter', kind=None),
                                                            Constant(value='message_unread_counter', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='public', kind=None),
                                                            Constant(value='rtcSessions', kind=None),
                                                            Constant(value='seen_message_id', kind=None),
                                                            Constant(value='state', kind=None),
                                                            Constant(value='uuid', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='channel_channel_group_1', ctx=Load()),
                                                                    attr='_get_avatar_cache_key',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            Constant(value='channel', kind=None),
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
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_channel_group_1', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
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
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=True, kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='channel_channel_group_1', ctx=Load()),
                                                                                    attr='channel_last_seen_partner_ids',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='filtered',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Lambda(
                                                                                    args=arguments(
                                                                                        posonlyargs=[],
                                                                                        args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                                        vararg=None,
                                                                                        kwonlyargs=[],
                                                                                        kw_defaults=[],
                                                                                        kwarg=None,
                                                                                        defaults=[],
                                                                                    ),
                                                                                    body=Compare(
                                                                                        left=Attribute(
                                                                                            value=Name(id='p', ctx=Load()),
                                                                                            attr='partner_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[
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
                                                                                                attr='partner_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='last_interest_dt',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='strftime',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='DEFAULT_SERVER_DATETIME_FORMAT', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Name(id='next', ctx=Load()),
                                                                args=[
                                                                    GeneratorExp(
                                                                        elt=Subscript(
                                                                            value=Name(id='res', ctx=Load()),
                                                                            slice=Constant(value='message_id', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='res', ctx=Store()),
                                                                                iter=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='channel_channel_group_1', ctx=Load()),
                                                                                        attr='_channel_last_message_ids',
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
                                                            Constant(value=5, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='group 1', kind=None),
                                                            Constant(value='groups', kind=None),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Name(id='next', ctx=Load()),
                                                                args=[
                                                                    GeneratorExp(
                                                                        elt=Subscript(
                                                                            value=Name(id='res', ctx=Load()),
                                                                            slice=Constant(value='message_id', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='res', ctx=Store()),
                                                                                iter=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='channel_channel_group_1', ctx=Load()),
                                                                                        attr='_channel_last_message_ids',
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
                                                            Constant(value='open', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_channel_group_1', ctx=Load()),
                                                                attr='uuid',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='avatarCacheKey', kind=None),
                                                            Constant(value='channel_type', kind=None),
                                                            Constant(value='create_uid', kind=None),
                                                            Constant(value='custom_channel_name', kind=None),
                                                            Constant(value='defaultDisplayMode', kind=None),
                                                            Constant(value='description', kind=None),
                                                            Constant(value='group_based_subscription', kind=None),
                                                            Constant(value='id', kind=None),
                                                            Constant(value='invitedGuests', kind=None),
                                                            Constant(value='invitedPartners', kind=None),
                                                            Constant(value='is_minimized', kind=None),
                                                            Constant(value='is_pinned', kind=None),
                                                            Constant(value='last_interest_dt', kind=None),
                                                            Constant(value='last_message_id', kind=None),
                                                            Constant(value='memberCount', kind=None),
                                                            Constant(value='message_needaction_counter', kind=None),
                                                            Constant(value='message_unread_counter', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='public', kind=None),
                                                            Constant(value='rtcSessions', kind=None),
                                                            Constant(value='seen_message_id', kind=None),
                                                            Constant(value='state', kind=None),
                                                            Constant(value='uuid', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='channel_channel_group_2', ctx=Load()),
                                                                    attr='_get_avatar_cache_key',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            Constant(value='channel', kind=None),
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
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_channel_group_2', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
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
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=True, kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='channel_channel_group_2', ctx=Load()),
                                                                                    attr='channel_last_seen_partner_ids',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='filtered',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Lambda(
                                                                                    args=arguments(
                                                                                        posonlyargs=[],
                                                                                        args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                                        vararg=None,
                                                                                        kwonlyargs=[],
                                                                                        kw_defaults=[],
                                                                                        kwarg=None,
                                                                                        defaults=[],
                                                                                    ),
                                                                                    body=Compare(
                                                                                        left=Attribute(
                                                                                            value=Name(id='p', ctx=Load()),
                                                                                            attr='partner_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[
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
                                                                                                attr='partner_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='last_interest_dt',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='strftime',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='DEFAULT_SERVER_DATETIME_FORMAT', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Name(id='next', ctx=Load()),
                                                                args=[
                                                                    GeneratorExp(
                                                                        elt=Subscript(
                                                                            value=Name(id='res', ctx=Load()),
                                                                            slice=Constant(value='message_id', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='res', ctx=Store()),
                                                                                iter=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='channel_channel_group_2', ctx=Load()),
                                                                                        attr='_channel_last_message_ids',
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
                                                            Constant(value=5, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='group 2', kind=None),
                                                            Constant(value='groups', kind=None),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Name(id='next', ctx=Load()),
                                                                args=[
                                                                    GeneratorExp(
                                                                        elt=Subscript(
                                                                            value=Name(id='res', ctx=Load()),
                                                                            slice=Constant(value='message_id', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='res', ctx=Store()),
                                                                                iter=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='channel_channel_group_2', ctx=Load()),
                                                                                        attr='_channel_last_message_ids',
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
                                                            Constant(value='open', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_channel_group_2', ctx=Load()),
                                                                attr='uuid',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='avatarCacheKey', kind=None),
                                                            Constant(value='channel_type', kind=None),
                                                            Constant(value='create_uid', kind=None),
                                                            Constant(value='custom_channel_name', kind=None),
                                                            Constant(value='defaultDisplayMode', kind=None),
                                                            Constant(value='description', kind=None),
                                                            Constant(value='group_based_subscription', kind=None),
                                                            Constant(value='id', kind=None),
                                                            Constant(value='invitedGuests', kind=None),
                                                            Constant(value='invitedPartners', kind=None),
                                                            Constant(value='is_minimized', kind=None),
                                                            Constant(value='is_pinned', kind=None),
                                                            Constant(value='last_interest_dt', kind=None),
                                                            Constant(value='last_message_id', kind=None),
                                                            Constant(value='memberCount', kind=None),
                                                            Constant(value='message_needaction_counter', kind=None),
                                                            Constant(value='message_unread_counter', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='public', kind=None),
                                                            Constant(value='rtcSessions', kind=None),
                                                            Constant(value='seen_message_id', kind=None),
                                                            Constant(value='state', kind=None),
                                                            Constant(value='uuid', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='channel_channel_private_1', ctx=Load()),
                                                                    attr='_get_avatar_cache_key',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            Constant(value='channel', kind=None),
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
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_channel_private_1', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
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
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=True, kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='channel_channel_private_1', ctx=Load()),
                                                                                    attr='channel_last_seen_partner_ids',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='filtered',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Lambda(
                                                                                    args=arguments(
                                                                                        posonlyargs=[],
                                                                                        args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                                        vararg=None,
                                                                                        kwonlyargs=[],
                                                                                        kw_defaults=[],
                                                                                        kwarg=None,
                                                                                        defaults=[],
                                                                                    ),
                                                                                    body=Compare(
                                                                                        left=Attribute(
                                                                                            value=Name(id='p', ctx=Load()),
                                                                                            attr='partner_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[
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
                                                                                                attr='partner_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='last_interest_dt',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='strftime',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='DEFAULT_SERVER_DATETIME_FORMAT', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Name(id='next', ctx=Load()),
                                                                args=[
                                                                    GeneratorExp(
                                                                        elt=Subscript(
                                                                            value=Name(id='res', ctx=Load()),
                                                                            slice=Constant(value='message_id', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='res', ctx=Store()),
                                                                                iter=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='channel_channel_private_1', ctx=Load()),
                                                                                        attr='_channel_last_message_ids',
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
                                                            Constant(value=5, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='private 1', kind=None),
                                                            Constant(value='private', kind=None),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Name(id='next', ctx=Load()),
                                                                args=[
                                                                    GeneratorExp(
                                                                        elt=Subscript(
                                                                            value=Name(id='res', ctx=Load()),
                                                                            slice=Constant(value='message_id', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='res', ctx=Store()),
                                                                                iter=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='channel_channel_private_1', ctx=Load()),
                                                                                        attr='_channel_last_message_ids',
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
                                                            Constant(value='open', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_channel_private_1', ctx=Load()),
                                                                attr='uuid',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='avatarCacheKey', kind=None),
                                                            Constant(value='channel_type', kind=None),
                                                            Constant(value='create_uid', kind=None),
                                                            Constant(value='custom_channel_name', kind=None),
                                                            Constant(value='defaultDisplayMode', kind=None),
                                                            Constant(value='description', kind=None),
                                                            Constant(value='group_based_subscription', kind=None),
                                                            Constant(value='id', kind=None),
                                                            Constant(value='invitedGuests', kind=None),
                                                            Constant(value='invitedPartners', kind=None),
                                                            Constant(value='is_minimized', kind=None),
                                                            Constant(value='is_pinned', kind=None),
                                                            Constant(value='last_interest_dt', kind=None),
                                                            Constant(value='last_message_id', kind=None),
                                                            Constant(value='memberCount', kind=None),
                                                            Constant(value='message_needaction_counter', kind=None),
                                                            Constant(value='message_unread_counter', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='public', kind=None),
                                                            Constant(value='rtcSessions', kind=None),
                                                            Constant(value='seen_message_id', kind=None),
                                                            Constant(value='state', kind=None),
                                                            Constant(value='uuid', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='channel_channel_private_2', ctx=Load()),
                                                                    attr='_get_avatar_cache_key',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            Constant(value='channel', kind=None),
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
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_channel_private_2', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
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
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=True, kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='channel_channel_private_2', ctx=Load()),
                                                                                    attr='channel_last_seen_partner_ids',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='filtered',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Lambda(
                                                                                    args=arguments(
                                                                                        posonlyargs=[],
                                                                                        args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                                        vararg=None,
                                                                                        kwonlyargs=[],
                                                                                        kw_defaults=[],
                                                                                        kwarg=None,
                                                                                        defaults=[],
                                                                                    ),
                                                                                    body=Compare(
                                                                                        left=Attribute(
                                                                                            value=Name(id='p', ctx=Load()),
                                                                                            attr='partner_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[
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
                                                                                                attr='partner_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='last_interest_dt',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='strftime',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='DEFAULT_SERVER_DATETIME_FORMAT', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Name(id='next', ctx=Load()),
                                                                args=[
                                                                    GeneratorExp(
                                                                        elt=Subscript(
                                                                            value=Name(id='res', ctx=Load()),
                                                                            slice=Constant(value='message_id', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='res', ctx=Store()),
                                                                                iter=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='channel_channel_private_2', ctx=Load()),
                                                                                        attr='_channel_last_message_ids',
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
                                                            Constant(value=5, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='private 2', kind=None),
                                                            Constant(value='private', kind=None),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Name(id='next', ctx=Load()),
                                                                args=[
                                                                    GeneratorExp(
                                                                        elt=Subscript(
                                                                            value=Name(id='res', ctx=Load()),
                                                                            slice=Constant(value='message_id', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='res', ctx=Store()),
                                                                                iter=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='channel_channel_private_2', ctx=Load()),
                                                                                        attr='_channel_last_message_ids',
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
                                                            Constant(value='open', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_channel_private_2', ctx=Load()),
                                                                attr='uuid',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='avatarCacheKey', kind=None),
                                                            Constant(value='channel_type', kind=None),
                                                            Constant(value='create_uid', kind=None),
                                                            Constant(value='custom_channel_name', kind=None),
                                                            Constant(value='defaultDisplayMode', kind=None),
                                                            Constant(value='description', kind=None),
                                                            Constant(value='group_based_subscription', kind=None),
                                                            Constant(value='id', kind=None),
                                                            Constant(value='invitedGuests', kind=None),
                                                            Constant(value='invitedPartners', kind=None),
                                                            Constant(value='is_minimized', kind=None),
                                                            Constant(value='is_pinned', kind=None),
                                                            Constant(value='last_interest_dt', kind=None),
                                                            Constant(value='last_message_id', kind=None),
                                                            Constant(value='memberCount', kind=None),
                                                            Constant(value='members', kind=None),
                                                            Constant(value='message_needaction_counter', kind=None),
                                                            Constant(value='message_unread_counter', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='public', kind=None),
                                                            Constant(value='rtcSessions', kind=None),
                                                            Constant(value='seen_message_id', kind=None),
                                                            Constant(value='seen_partners_info', kind=None),
                                                            Constant(value='state', kind=None),
                                                            Constant(value='uuid', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='channel_group_1', ctx=Load()),
                                                                    attr='_get_avatar_cache_key',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            Constant(value='group', kind=None),
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
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_group_1', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
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
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=True, kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='channel_group_1', ctx=Load()),
                                                                                    attr='channel_last_seen_partner_ids',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='filtered',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Lambda(
                                                                                    args=arguments(
                                                                                        posonlyargs=[],
                                                                                        args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                                        vararg=None,
                                                                                        kwonlyargs=[],
                                                                                        kw_defaults=[],
                                                                                        kwarg=None,
                                                                                        defaults=[],
                                                                                    ),
                                                                                    body=Compare(
                                                                                        left=Attribute(
                                                                                            value=Name(id='p', ctx=Load()),
                                                                                            attr='partner_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[
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
                                                                                                attr='partner_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='last_interest_dt',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='strftime',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='DEFAULT_SERVER_DATETIME_FORMAT', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=2, kind=None),
                                                            List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='active', kind=None),
                                                                            Constant(value='display_name', kind=None),
                                                                            Constant(value='email', kind=None),
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='im_status', kind=None),
                                                                            Constant(value='is_internal_user', kind=None),
                                                                            Constant(value='name', kind=None),
                                                                            Constant(value='out_of_office_date_end', kind=None),
                                                                            Constant(value='user_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=True, kind=None),
                                                                            Constant(value='Ernest Employee', kind=None),
                                                                            Constant(value='e.e@example.com', kind=None),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='users',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='leave_offline', kind=None),
                                                                            Constant(value=True, kind=None),
                                                                            Constant(value='Ernest Employee', kind=None),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Call(
                                                                                            func=Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='leaves',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='filtered',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[
                                                                                                Lambda(
                                                                                                    args=arguments(
                                                                                                        posonlyargs=[],
                                                                                                        args=[arg(arg='l', annotation=None, type_comment=None)],
                                                                                                        vararg=None,
                                                                                                        kwonlyargs=[],
                                                                                                        kw_defaults=[],
                                                                                                        kwarg=None,
                                                                                                        defaults=[],
                                                                                                    ),
                                                                                                    body=Compare(
                                                                                                        left=Attribute(
                                                                                                            value=Attribute(
                                                                                                                value=Name(id='l', ctx=Load()),
                                                                                                                attr='employee_id',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            attr='user_id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        ops=[Eq()],
                                                                                                        comparators=[
                                                                                                            Subscript(
                                                                                                                value=Attribute(
                                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                                    attr='users',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                slice=Constant(value=0, kind=None),
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                ),
                                                                                            ],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        attr='date_to',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='strftime',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='DEFAULT_SERVER_DATE_FORMAT', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
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
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='active', kind=None),
                                                                            Constant(value='display_name', kind=None),
                                                                            Constant(value='email', kind=None),
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='im_status', kind=None),
                                                                            Constant(value='is_internal_user', kind=None),
                                                                            Constant(value='name', kind=None),
                                                                            Constant(value='out_of_office_date_end', kind=None),
                                                                            Constant(value='user_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=True, kind=None),
                                                                            Constant(value='test12', kind=None),
                                                                            Constant(value=False, kind=None),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='users',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value=12, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='leave_offline', kind=None),
                                                                            Constant(value=True, kind=None),
                                                                            Constant(value='test12', kind=None),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Call(
                                                                                            func=Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='leaves',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='filtered',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[
                                                                                                Lambda(
                                                                                                    args=arguments(
                                                                                                        posonlyargs=[],
                                                                                                        args=[arg(arg='l', annotation=None, type_comment=None)],
                                                                                                        vararg=None,
                                                                                                        kwonlyargs=[],
                                                                                                        kw_defaults=[],
                                                                                                        kwarg=None,
                                                                                                        defaults=[],
                                                                                                    ),
                                                                                                    body=Compare(
                                                                                                        left=Attribute(
                                                                                                            value=Attribute(
                                                                                                                value=Name(id='l', ctx=Load()),
                                                                                                                attr='employee_id',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            attr='user_id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        ops=[Eq()],
                                                                                                        comparators=[
                                                                                                            Subscript(
                                                                                                                value=Attribute(
                                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                                    attr='users',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                slice=Constant(value=12, kind=None),
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                ),
                                                                                            ],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        attr='date_to',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='strftime',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='DEFAULT_SERVER_DATE_FORMAT', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                            Attribute(
                                                                                value=Subscript(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='users',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Constant(value=12, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='', kind=None),
                                                            Constant(value='private', kind=None),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='fetched_message_id', kind=None),
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='seen_message_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=False, kind=None),
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='channel_group_1', ctx=Load()),
                                                                                            attr='channel_last_seen_partner_ids',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='filtered',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[
                                                                                        Lambda(
                                                                                            args=arguments(
                                                                                                posonlyargs=[],
                                                                                                args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                                                vararg=None,
                                                                                                kwonlyargs=[],
                                                                                                kw_defaults=[],
                                                                                                kwarg=None,
                                                                                                defaults=[],
                                                                                            ),
                                                                                            body=Compare(
                                                                                                left=Attribute(
                                                                                                    value=Name(id='p', ctx=Load()),
                                                                                                    attr='partner_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[Eq()],
                                                                                                comparators=[
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
                                                                                                        attr='partner_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='users',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='fetched_message_id', kind=None),
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='seen_message_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=False, kind=None),
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='channel_group_1', ctx=Load()),
                                                                                            attr='channel_last_seen_partner_ids',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='filtered',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[
                                                                                        Lambda(
                                                                                            args=arguments(
                                                                                                posonlyargs=[],
                                                                                                args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                                                vararg=None,
                                                                                                kwonlyargs=[],
                                                                                                kw_defaults=[],
                                                                                                kwarg=None,
                                                                                                defaults=[],
                                                                                            ),
                                                                                            body=Compare(
                                                                                                left=Attribute(
                                                                                                    value=Name(id='p', ctx=Load()),
                                                                                                    attr='partner_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[Eq()],
                                                                                                comparators=[
                                                                                                    Attribute(
                                                                                                        value=Subscript(
                                                                                                            value=Attribute(
                                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                                attr='users',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            slice=Constant(value=12, kind=None),
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='partner_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='users',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value=12, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='open', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_group_1', ctx=Load()),
                                                                attr='uuid',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='avatarCacheKey', kind=None),
                                                            Constant(value='channel_type', kind=None),
                                                            Constant(value='create_uid', kind=None),
                                                            Constant(value='custom_channel_name', kind=None),
                                                            Constant(value='defaultDisplayMode', kind=None),
                                                            Constant(value='description', kind=None),
                                                            Constant(value='group_based_subscription', kind=None),
                                                            Constant(value='id', kind=None),
                                                            Constant(value='invitedGuests', kind=None),
                                                            Constant(value='invitedPartners', kind=None),
                                                            Constant(value='is_minimized', kind=None),
                                                            Constant(value='is_pinned', kind=None),
                                                            Constant(value='last_interest_dt', kind=None),
                                                            Constant(value='last_message_id', kind=None),
                                                            Constant(value='memberCount', kind=None),
                                                            Constant(value='members', kind=None),
                                                            Constant(value='message_needaction_counter', kind=None),
                                                            Constant(value='message_unread_counter', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='public', kind=None),
                                                            Constant(value='rtcSessions', kind=None),
                                                            Constant(value='seen_partners_info', kind=None),
                                                            Constant(value='seen_message_id', kind=None),
                                                            Constant(value='state', kind=None),
                                                            Constant(value='uuid', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='channel_chat_1', ctx=Load()),
                                                                    attr='_get_avatar_cache_key',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            Constant(value='chat', kind=None),
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
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_chat_1', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
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
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=True, kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='channel_chat_1', ctx=Load()),
                                                                                    attr='channel_last_seen_partner_ids',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='filtered',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Lambda(
                                                                                    args=arguments(
                                                                                        posonlyargs=[],
                                                                                        args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                                        vararg=None,
                                                                                        kwonlyargs=[],
                                                                                        kw_defaults=[],
                                                                                        kwarg=None,
                                                                                        defaults=[],
                                                                                    ),
                                                                                    body=Compare(
                                                                                        left=Attribute(
                                                                                            value=Name(id='p', ctx=Load()),
                                                                                            attr='partner_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[
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
                                                                                                attr='partner_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='last_interest_dt',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='strftime',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='DEFAULT_SERVER_DATETIME_FORMAT', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=2, kind=None),
                                                            List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='active', kind=None),
                                                                            Constant(value='display_name', kind=None),
                                                                            Constant(value='email', kind=None),
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='im_status', kind=None),
                                                                            Constant(value='is_internal_user', kind=None),
                                                                            Constant(value='name', kind=None),
                                                                            Constant(value='out_of_office_date_end', kind=None),
                                                                            Constant(value='user_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=True, kind=None),
                                                                            Constant(value='Ernest Employee', kind=None),
                                                                            Constant(value='e.e@example.com', kind=None),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='users',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='leave_offline', kind=None),
                                                                            Constant(value=True, kind=None),
                                                                            Constant(value='Ernest Employee', kind=None),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Call(
                                                                                            func=Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='leaves',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='filtered',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[
                                                                                                Lambda(
                                                                                                    args=arguments(
                                                                                                        posonlyargs=[],
                                                                                                        args=[arg(arg='l', annotation=None, type_comment=None)],
                                                                                                        vararg=None,
                                                                                                        kwonlyargs=[],
                                                                                                        kw_defaults=[],
                                                                                                        kwarg=None,
                                                                                                        defaults=[],
                                                                                                    ),
                                                                                                    body=Compare(
                                                                                                        left=Attribute(
                                                                                                            value=Attribute(
                                                                                                                value=Name(id='l', ctx=Load()),
                                                                                                                attr='employee_id',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            attr='user_id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        ops=[Eq()],
                                                                                                        comparators=[
                                                                                                            Subscript(
                                                                                                                value=Attribute(
                                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                                    attr='users',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                slice=Constant(value=0, kind=None),
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                ),
                                                                                            ],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        attr='date_to',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='strftime',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='DEFAULT_SERVER_DATE_FORMAT', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
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
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='active', kind=None),
                                                                            Constant(value='display_name', kind=None),
                                                                            Constant(value='email', kind=None),
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='im_status', kind=None),
                                                                            Constant(value='is_internal_user', kind=None),
                                                                            Constant(value='name', kind=None),
                                                                            Constant(value='out_of_office_date_end', kind=None),
                                                                            Constant(value='user_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=True, kind=None),
                                                                            Constant(value='test14', kind=None),
                                                                            Constant(value=False, kind=None),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='users',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value=14, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='leave_offline', kind=None),
                                                                            Constant(value=True, kind=None),
                                                                            Constant(value='test14', kind=None),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Call(
                                                                                            func=Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='leaves',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='filtered',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[
                                                                                                Lambda(
                                                                                                    args=arguments(
                                                                                                        posonlyargs=[],
                                                                                                        args=[arg(arg='l', annotation=None, type_comment=None)],
                                                                                                        vararg=None,
                                                                                                        kwonlyargs=[],
                                                                                                        kw_defaults=[],
                                                                                                        kwarg=None,
                                                                                                        defaults=[],
                                                                                                    ),
                                                                                                    body=Compare(
                                                                                                        left=Attribute(
                                                                                                            value=Attribute(
                                                                                                                value=Name(id='l', ctx=Load()),
                                                                                                                attr='employee_id',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            attr='user_id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        ops=[Eq()],
                                                                                                        comparators=[
                                                                                                            Subscript(
                                                                                                                value=Attribute(
                                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                                    attr='users',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                slice=Constant(value=14, kind=None),
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                ),
                                                                                            ],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        attr='date_to',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='strftime',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='DEFAULT_SERVER_DATE_FORMAT', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                            Attribute(
                                                                                value=Subscript(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='users',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Constant(value=14, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='Ernest Employee, test14', kind=None),
                                                            Constant(value='private', kind=None),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
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
                                                                            Constant(value='fetched_message_id', kind=None),
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='seen_message_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=False, kind=None),
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='channel_chat_1', ctx=Load()),
                                                                                            attr='channel_last_seen_partner_ids',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='filtered',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[
                                                                                        Lambda(
                                                                                            args=arguments(
                                                                                                posonlyargs=[],
                                                                                                args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                                                vararg=None,
                                                                                                kwonlyargs=[],
                                                                                                kw_defaults=[],
                                                                                                kwarg=None,
                                                                                                defaults=[],
                                                                                            ),
                                                                                            body=Compare(
                                                                                                left=Attribute(
                                                                                                    value=Name(id='p', ctx=Load()),
                                                                                                    attr='partner_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[Eq()],
                                                                                                comparators=[
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
                                                                                                        attr='partner_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='users',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='fetched_message_id', kind=None),
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='seen_message_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=False, kind=None),
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='channel_chat_1', ctx=Load()),
                                                                                            attr='channel_last_seen_partner_ids',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='filtered',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[
                                                                                        Lambda(
                                                                                            args=arguments(
                                                                                                posonlyargs=[],
                                                                                                args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                                                vararg=None,
                                                                                                kwonlyargs=[],
                                                                                                kw_defaults=[],
                                                                                                kwarg=None,
                                                                                                defaults=[],
                                                                                            ),
                                                                                            body=Compare(
                                                                                                left=Attribute(
                                                                                                    value=Name(id='p', ctx=Load()),
                                                                                                    attr='partner_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[Eq()],
                                                                                                comparators=[
                                                                                                    Attribute(
                                                                                                        value=Subscript(
                                                                                                            value=Attribute(
                                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                                attr='users',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            slice=Constant(value=14, kind=None),
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='partner_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='users',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value=14, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value='open', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_chat_1', ctx=Load()),
                                                                attr='uuid',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='avatarCacheKey', kind=None),
                                                            Constant(value='channel_type', kind=None),
                                                            Constant(value='create_uid', kind=None),
                                                            Constant(value='custom_channel_name', kind=None),
                                                            Constant(value='defaultDisplayMode', kind=None),
                                                            Constant(value='description', kind=None),
                                                            Constant(value='group_based_subscription', kind=None),
                                                            Constant(value='id', kind=None),
                                                            Constant(value='invitedGuests', kind=None),
                                                            Constant(value='invitedPartners', kind=None),
                                                            Constant(value='is_minimized', kind=None),
                                                            Constant(value='is_pinned', kind=None),
                                                            Constant(value='last_interest_dt', kind=None),
                                                            Constant(value='last_message_id', kind=None),
                                                            Constant(value='memberCount', kind=None),
                                                            Constant(value='members', kind=None),
                                                            Constant(value='message_needaction_counter', kind=None),
                                                            Constant(value='message_unread_counter', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='public', kind=None),
                                                            Constant(value='rtcSessions', kind=None),
                                                            Constant(value='seen_partners_info', kind=None),
                                                            Constant(value='seen_message_id', kind=None),
                                                            Constant(value='state', kind=None),
                                                            Constant(value='uuid', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='channel_chat_2', ctx=Load()),
                                                                    attr='_get_avatar_cache_key',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            Constant(value='chat', kind=None),
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
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_chat_2', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
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
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=True, kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='channel_chat_2', ctx=Load()),
                                                                                    attr='channel_last_seen_partner_ids',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='filtered',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Lambda(
                                                                                    args=arguments(
                                                                                        posonlyargs=[],
                                                                                        args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                                        vararg=None,
                                                                                        kwonlyargs=[],
                                                                                        kw_defaults=[],
                                                                                        kwarg=None,
                                                                                        defaults=[],
                                                                                    ),
                                                                                    body=Compare(
                                                                                        left=Attribute(
                                                                                            value=Name(id='p', ctx=Load()),
                                                                                            attr='partner_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[
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
                                                                                                attr='partner_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='last_interest_dt',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='strftime',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='DEFAULT_SERVER_DATETIME_FORMAT', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=2, kind=None),
                                                            List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='active', kind=None),
                                                                            Constant(value='display_name', kind=None),
                                                                            Constant(value='email', kind=None),
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='im_status', kind=None),
                                                                            Constant(value='is_internal_user', kind=None),
                                                                            Constant(value='name', kind=None),
                                                                            Constant(value='out_of_office_date_end', kind=None),
                                                                            Constant(value='user_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=True, kind=None),
                                                                            Constant(value='Ernest Employee', kind=None),
                                                                            Constant(value='e.e@example.com', kind=None),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='users',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='leave_offline', kind=None),
                                                                            Constant(value=True, kind=None),
                                                                            Constant(value='Ernest Employee', kind=None),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Call(
                                                                                            func=Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='leaves',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='filtered',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[
                                                                                                Lambda(
                                                                                                    args=arguments(
                                                                                                        posonlyargs=[],
                                                                                                        args=[arg(arg='l', annotation=None, type_comment=None)],
                                                                                                        vararg=None,
                                                                                                        kwonlyargs=[],
                                                                                                        kw_defaults=[],
                                                                                                        kwarg=None,
                                                                                                        defaults=[],
                                                                                                    ),
                                                                                                    body=Compare(
                                                                                                        left=Attribute(
                                                                                                            value=Attribute(
                                                                                                                value=Name(id='l', ctx=Load()),
                                                                                                                attr='employee_id',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            attr='user_id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        ops=[Eq()],
                                                                                                        comparators=[
                                                                                                            Subscript(
                                                                                                                value=Attribute(
                                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                                    attr='users',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                slice=Constant(value=0, kind=None),
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                ),
                                                                                            ],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        attr='date_to',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='strftime',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='DEFAULT_SERVER_DATE_FORMAT', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
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
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='active', kind=None),
                                                                            Constant(value='display_name', kind=None),
                                                                            Constant(value='email', kind=None),
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='im_status', kind=None),
                                                                            Constant(value='is_internal_user', kind=None),
                                                                            Constant(value='name', kind=None),
                                                                            Constant(value='out_of_office_date_end', kind=None),
                                                                            Constant(value='user_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=True, kind=None),
                                                                            Constant(value='test15', kind=None),
                                                                            Constant(value=False, kind=None),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='users',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value=15, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='leave_offline', kind=None),
                                                                            Constant(value=True, kind=None),
                                                                            Constant(value='test15', kind=None),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Call(
                                                                                            func=Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='leaves',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='filtered',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[
                                                                                                Lambda(
                                                                                                    args=arguments(
                                                                                                        posonlyargs=[],
                                                                                                        args=[arg(arg='l', annotation=None, type_comment=None)],
                                                                                                        vararg=None,
                                                                                                        kwonlyargs=[],
                                                                                                        kw_defaults=[],
                                                                                                        kwarg=None,
                                                                                                        defaults=[],
                                                                                                    ),
                                                                                                    body=Compare(
                                                                                                        left=Attribute(
                                                                                                            value=Attribute(
                                                                                                                value=Name(id='l', ctx=Load()),
                                                                                                                attr='employee_id',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            attr='user_id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        ops=[Eq()],
                                                                                                        comparators=[
                                                                                                            Subscript(
                                                                                                                value=Attribute(
                                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                                    attr='users',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                slice=Constant(value=15, kind=None),
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                ),
                                                                                            ],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        attr='date_to',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='strftime',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='DEFAULT_SERVER_DATE_FORMAT', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                            Attribute(
                                                                                value=Subscript(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='users',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Constant(value=15, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='Ernest Employee, test15', kind=None),
                                                            Constant(value='private', kind=None),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
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
                                                                            Constant(value='fetched_message_id', kind=None),
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='seen_message_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=False, kind=None),
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='channel_chat_2', ctx=Load()),
                                                                                            attr='channel_last_seen_partner_ids',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='filtered',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[
                                                                                        Lambda(
                                                                                            args=arguments(
                                                                                                posonlyargs=[],
                                                                                                args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                                                vararg=None,
                                                                                                kwonlyargs=[],
                                                                                                kw_defaults=[],
                                                                                                kwarg=None,
                                                                                                defaults=[],
                                                                                            ),
                                                                                            body=Compare(
                                                                                                left=Attribute(
                                                                                                    value=Name(id='p', ctx=Load()),
                                                                                                    attr='partner_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[Eq()],
                                                                                                comparators=[
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
                                                                                                        attr='partner_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='users',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='fetched_message_id', kind=None),
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='seen_message_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=False, kind=None),
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='channel_chat_2', ctx=Load()),
                                                                                            attr='channel_last_seen_partner_ids',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='filtered',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[
                                                                                        Lambda(
                                                                                            args=arguments(
                                                                                                posonlyargs=[],
                                                                                                args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                                                vararg=None,
                                                                                                kwonlyargs=[],
                                                                                                kw_defaults=[],
                                                                                                kwarg=None,
                                                                                                defaults=[],
                                                                                            ),
                                                                                            body=Compare(
                                                                                                left=Attribute(
                                                                                                    value=Name(id='p', ctx=Load()),
                                                                                                    attr='partner_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[Eq()],
                                                                                                comparators=[
                                                                                                    Attribute(
                                                                                                        value=Subscript(
                                                                                                            value=Attribute(
                                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                                attr='users',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            slice=Constant(value=15, kind=None),
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='partner_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='users',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value=15, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value='open', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_chat_2', ctx=Load()),
                                                                attr='uuid',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='avatarCacheKey', kind=None),
                                                            Constant(value='channel_type', kind=None),
                                                            Constant(value='create_uid', kind=None),
                                                            Constant(value='custom_channel_name', kind=None),
                                                            Constant(value='defaultDisplayMode', kind=None),
                                                            Constant(value='description', kind=None),
                                                            Constant(value='group_based_subscription', kind=None),
                                                            Constant(value='id', kind=None),
                                                            Constant(value='invitedGuests', kind=None),
                                                            Constant(value='invitedPartners', kind=None),
                                                            Constant(value='is_minimized', kind=None),
                                                            Constant(value='is_pinned', kind=None),
                                                            Constant(value='last_interest_dt', kind=None),
                                                            Constant(value='last_message_id', kind=None),
                                                            Constant(value='memberCount', kind=None),
                                                            Constant(value='members', kind=None),
                                                            Constant(value='message_needaction_counter', kind=None),
                                                            Constant(value='message_unread_counter', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='public', kind=None),
                                                            Constant(value='rtcSessions', kind=None),
                                                            Constant(value='seen_partners_info', kind=None),
                                                            Constant(value='seen_message_id', kind=None),
                                                            Constant(value='state', kind=None),
                                                            Constant(value='uuid', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='channel_chat_3', ctx=Load()),
                                                                    attr='_get_avatar_cache_key',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            Constant(value='chat', kind=None),
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
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_chat_3', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
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
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=True, kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='channel_chat_3', ctx=Load()),
                                                                                    attr='channel_last_seen_partner_ids',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='filtered',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Lambda(
                                                                                    args=arguments(
                                                                                        posonlyargs=[],
                                                                                        args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                                        vararg=None,
                                                                                        kwonlyargs=[],
                                                                                        kw_defaults=[],
                                                                                        kwarg=None,
                                                                                        defaults=[],
                                                                                    ),
                                                                                    body=Compare(
                                                                                        left=Attribute(
                                                                                            value=Name(id='p', ctx=Load()),
                                                                                            attr='partner_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[
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
                                                                                                attr='partner_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='last_interest_dt',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='strftime',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='DEFAULT_SERVER_DATETIME_FORMAT', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=2, kind=None),
                                                            List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='active', kind=None),
                                                                            Constant(value='display_name', kind=None),
                                                                            Constant(value='email', kind=None),
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='im_status', kind=None),
                                                                            Constant(value='is_internal_user', kind=None),
                                                                            Constant(value='name', kind=None),
                                                                            Constant(value='out_of_office_date_end', kind=None),
                                                                            Constant(value='user_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=True, kind=None),
                                                                            Constant(value='Ernest Employee', kind=None),
                                                                            Constant(value='e.e@example.com', kind=None),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='users',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='leave_offline', kind=None),
                                                                            Constant(value=True, kind=None),
                                                                            Constant(value='Ernest Employee', kind=None),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Call(
                                                                                            func=Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='leaves',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='filtered',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[
                                                                                                Lambda(
                                                                                                    args=arguments(
                                                                                                        posonlyargs=[],
                                                                                                        args=[arg(arg='l', annotation=None, type_comment=None)],
                                                                                                        vararg=None,
                                                                                                        kwonlyargs=[],
                                                                                                        kw_defaults=[],
                                                                                                        kwarg=None,
                                                                                                        defaults=[],
                                                                                                    ),
                                                                                                    body=Compare(
                                                                                                        left=Attribute(
                                                                                                            value=Attribute(
                                                                                                                value=Name(id='l', ctx=Load()),
                                                                                                                attr='employee_id',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            attr='user_id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        ops=[Eq()],
                                                                                                        comparators=[
                                                                                                            Subscript(
                                                                                                                value=Attribute(
                                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                                    attr='users',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                slice=Constant(value=0, kind=None),
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                ),
                                                                                            ],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        attr='date_to',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='strftime',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='DEFAULT_SERVER_DATE_FORMAT', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
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
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='active', kind=None),
                                                                            Constant(value='display_name', kind=None),
                                                                            Constant(value='email', kind=None),
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='im_status', kind=None),
                                                                            Constant(value='is_internal_user', kind=None),
                                                                            Constant(value='name', kind=None),
                                                                            Constant(value='out_of_office_date_end', kind=None),
                                                                            Constant(value='user_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=True, kind=None),
                                                                            Constant(value='test2', kind=None),
                                                                            Constant(value='test2@example.com', kind=None),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='users',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value=2, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='leave_offline', kind=None),
                                                                            Constant(value=True, kind=None),
                                                                            Constant(value='test2', kind=None),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Call(
                                                                                            func=Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='leaves',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='filtered',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[
                                                                                                Lambda(
                                                                                                    args=arguments(
                                                                                                        posonlyargs=[],
                                                                                                        args=[arg(arg='l', annotation=None, type_comment=None)],
                                                                                                        vararg=None,
                                                                                                        kwonlyargs=[],
                                                                                                        kw_defaults=[],
                                                                                                        kwarg=None,
                                                                                                        defaults=[],
                                                                                                    ),
                                                                                                    body=Compare(
                                                                                                        left=Attribute(
                                                                                                            value=Attribute(
                                                                                                                value=Name(id='l', ctx=Load()),
                                                                                                                attr='employee_id',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            attr='user_id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        ops=[Eq()],
                                                                                                        comparators=[
                                                                                                            Subscript(
                                                                                                                value=Attribute(
                                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                                    attr='users',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                slice=Constant(value=2, kind=None),
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                ),
                                                                                            ],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        attr='date_to',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='strftime',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='DEFAULT_SERVER_DATE_FORMAT', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                            Attribute(
                                                                                value=Subscript(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='users',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Constant(value=2, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='Ernest Employee, test2', kind=None),
                                                            Constant(value='private', kind=None),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
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
                                                                            Constant(value='fetched_message_id', kind=None),
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='seen_message_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=False, kind=None),
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='channel_chat_3', ctx=Load()),
                                                                                            attr='channel_last_seen_partner_ids',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='filtered',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[
                                                                                        Lambda(
                                                                                            args=arguments(
                                                                                                posonlyargs=[],
                                                                                                args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                                                vararg=None,
                                                                                                kwonlyargs=[],
                                                                                                kw_defaults=[],
                                                                                                kwarg=None,
                                                                                                defaults=[],
                                                                                            ),
                                                                                            body=Compare(
                                                                                                left=Attribute(
                                                                                                    value=Name(id='p', ctx=Load()),
                                                                                                    attr='partner_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[Eq()],
                                                                                                comparators=[
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
                                                                                                        attr='partner_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='users',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='fetched_message_id', kind=None),
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='seen_message_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=False, kind=None),
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='channel_chat_3', ctx=Load()),
                                                                                            attr='channel_last_seen_partner_ids',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='filtered',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[
                                                                                        Lambda(
                                                                                            args=arguments(
                                                                                                posonlyargs=[],
                                                                                                args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                                                vararg=None,
                                                                                                kwonlyargs=[],
                                                                                                kw_defaults=[],
                                                                                                kwarg=None,
                                                                                                defaults=[],
                                                                                            ),
                                                                                            body=Compare(
                                                                                                left=Attribute(
                                                                                                    value=Name(id='p', ctx=Load()),
                                                                                                    attr='partner_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[Eq()],
                                                                                                comparators=[
                                                                                                    Attribute(
                                                                                                        value=Subscript(
                                                                                                            value=Attribute(
                                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                                attr='users',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            slice=Constant(value=2, kind=None),
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='partner_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='users',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value=2, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value='open', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_chat_3', ctx=Load()),
                                                                attr='uuid',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='avatarCacheKey', kind=None),
                                                            Constant(value='channel_type', kind=None),
                                                            Constant(value='create_uid', kind=None),
                                                            Constant(value='custom_channel_name', kind=None),
                                                            Constant(value='defaultDisplayMode', kind=None),
                                                            Constant(value='description', kind=None),
                                                            Constant(value='group_based_subscription', kind=None),
                                                            Constant(value='id', kind=None),
                                                            Constant(value='invitedGuests', kind=None),
                                                            Constant(value='invitedPartners', kind=None),
                                                            Constant(value='is_minimized', kind=None),
                                                            Constant(value='is_pinned', kind=None),
                                                            Constant(value='last_interest_dt', kind=None),
                                                            Constant(value='last_message_id', kind=None),
                                                            Constant(value='memberCount', kind=None),
                                                            Constant(value='members', kind=None),
                                                            Constant(value='message_needaction_counter', kind=None),
                                                            Constant(value='message_unread_counter', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='public', kind=None),
                                                            Constant(value='rtcSessions', kind=None),
                                                            Constant(value='seen_partners_info', kind=None),
                                                            Constant(value='seen_message_id', kind=None),
                                                            Constant(value='state', kind=None),
                                                            Constant(value='uuid', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='channel_chat_4', ctx=Load()),
                                                                    attr='_get_avatar_cache_key',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            Constant(value='chat', kind=None),
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
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_chat_4', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
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
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=True, kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='channel_chat_4', ctx=Load()),
                                                                                    attr='channel_last_seen_partner_ids',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='filtered',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Lambda(
                                                                                    args=arguments(
                                                                                        posonlyargs=[],
                                                                                        args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                                        vararg=None,
                                                                                        kwonlyargs=[],
                                                                                        kw_defaults=[],
                                                                                        kwarg=None,
                                                                                        defaults=[],
                                                                                    ),
                                                                                    body=Compare(
                                                                                        left=Attribute(
                                                                                            value=Name(id='p', ctx=Load()),
                                                                                            attr='partner_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[
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
                                                                                                attr='partner_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='last_interest_dt',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='strftime',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='DEFAULT_SERVER_DATETIME_FORMAT', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=2, kind=None),
                                                            List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='active', kind=None),
                                                                            Constant(value='display_name', kind=None),
                                                                            Constant(value='email', kind=None),
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='im_status', kind=None),
                                                                            Constant(value='is_internal_user', kind=None),
                                                                            Constant(value='name', kind=None),
                                                                            Constant(value='out_of_office_date_end', kind=None),
                                                                            Constant(value='user_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=True, kind=None),
                                                                            Constant(value='Ernest Employee', kind=None),
                                                                            Constant(value='e.e@example.com', kind=None),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='users',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='leave_offline', kind=None),
                                                                            Constant(value=True, kind=None),
                                                                            Constant(value='Ernest Employee', kind=None),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Call(
                                                                                            func=Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='leaves',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='filtered',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[
                                                                                                Lambda(
                                                                                                    args=arguments(
                                                                                                        posonlyargs=[],
                                                                                                        args=[arg(arg='l', annotation=None, type_comment=None)],
                                                                                                        vararg=None,
                                                                                                        kwonlyargs=[],
                                                                                                        kw_defaults=[],
                                                                                                        kwarg=None,
                                                                                                        defaults=[],
                                                                                                    ),
                                                                                                    body=Compare(
                                                                                                        left=Attribute(
                                                                                                            value=Attribute(
                                                                                                                value=Name(id='l', ctx=Load()),
                                                                                                                attr='employee_id',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            attr='user_id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        ops=[Eq()],
                                                                                                        comparators=[
                                                                                                            Subscript(
                                                                                                                value=Attribute(
                                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                                    attr='users',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                slice=Constant(value=0, kind=None),
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                ),
                                                                                            ],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        attr='date_to',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='strftime',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='DEFAULT_SERVER_DATE_FORMAT', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
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
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='active', kind=None),
                                                                            Constant(value='display_name', kind=None),
                                                                            Constant(value='email', kind=None),
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='im_status', kind=None),
                                                                            Constant(value='is_internal_user', kind=None),
                                                                            Constant(value='name', kind=None),
                                                                            Constant(value='out_of_office_date_end', kind=None),
                                                                            Constant(value='user_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=True, kind=None),
                                                                            Constant(value='test3', kind=None),
                                                                            Constant(value=False, kind=None),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='users',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value=3, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='leave_offline', kind=None),
                                                                            Constant(value=True, kind=None),
                                                                            Constant(value='test3', kind=None),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Call(
                                                                                            func=Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='leaves',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='filtered',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[
                                                                                                Lambda(
                                                                                                    args=arguments(
                                                                                                        posonlyargs=[],
                                                                                                        args=[arg(arg='l', annotation=None, type_comment=None)],
                                                                                                        vararg=None,
                                                                                                        kwonlyargs=[],
                                                                                                        kw_defaults=[],
                                                                                                        kwarg=None,
                                                                                                        defaults=[],
                                                                                                    ),
                                                                                                    body=Compare(
                                                                                                        left=Attribute(
                                                                                                            value=Attribute(
                                                                                                                value=Name(id='l', ctx=Load()),
                                                                                                                attr='employee_id',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            attr='user_id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        ops=[Eq()],
                                                                                                        comparators=[
                                                                                                            Subscript(
                                                                                                                value=Attribute(
                                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                                    attr='users',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                slice=Constant(value=3, kind=None),
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                ),
                                                                                            ],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        attr='date_to',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='strftime',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='DEFAULT_SERVER_DATE_FORMAT', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                            Attribute(
                                                                                value=Subscript(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='users',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Constant(value=3, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='Ernest Employee, test3', kind=None),
                                                            Constant(value='private', kind=None),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
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
                                                                            Constant(value='fetched_message_id', kind=None),
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='seen_message_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=False, kind=None),
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='channel_chat_4', ctx=Load()),
                                                                                            attr='channel_last_seen_partner_ids',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='filtered',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[
                                                                                        Lambda(
                                                                                            args=arguments(
                                                                                                posonlyargs=[],
                                                                                                args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                                                vararg=None,
                                                                                                kwonlyargs=[],
                                                                                                kw_defaults=[],
                                                                                                kwarg=None,
                                                                                                defaults=[],
                                                                                            ),
                                                                                            body=Compare(
                                                                                                left=Attribute(
                                                                                                    value=Name(id='p', ctx=Load()),
                                                                                                    attr='partner_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[Eq()],
                                                                                                comparators=[
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
                                                                                                        attr='partner_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='users',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='fetched_message_id', kind=None),
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='seen_message_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=False, kind=None),
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='channel_chat_4', ctx=Load()),
                                                                                            attr='channel_last_seen_partner_ids',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='filtered',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[
                                                                                        Lambda(
                                                                                            args=arguments(
                                                                                                posonlyargs=[],
                                                                                                args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                                                vararg=None,
                                                                                                kwonlyargs=[],
                                                                                                kw_defaults=[],
                                                                                                kwarg=None,
                                                                                                defaults=[],
                                                                                            ),
                                                                                            body=Compare(
                                                                                                left=Attribute(
                                                                                                    value=Name(id='p', ctx=Load()),
                                                                                                    attr='partner_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[Eq()],
                                                                                                comparators=[
                                                                                                    Attribute(
                                                                                                        value=Subscript(
                                                                                                            value=Attribute(
                                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                                attr='users',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            slice=Constant(value=3, kind=None),
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='partner_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='users',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value=3, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value='open', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_chat_4', ctx=Load()),
                                                                attr='uuid',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='avatarCacheKey', kind=None),
                                                            Constant(value='channel_type', kind=None),
                                                            Constant(value='create_uid', kind=None),
                                                            Constant(value='custom_channel_name', kind=None),
                                                            Constant(value='defaultDisplayMode', kind=None),
                                                            Constant(value='description', kind=None),
                                                            Constant(value='group_based_subscription', kind=None),
                                                            Constant(value='id', kind=None),
                                                            Constant(value='invitedGuests', kind=None),
                                                            Constant(value='invitedPartners', kind=None),
                                                            Constant(value='is_minimized', kind=None),
                                                            Constant(value='is_pinned', kind=None),
                                                            Constant(value='last_interest_dt', kind=None),
                                                            Constant(value='last_message_id', kind=None),
                                                            Constant(value='memberCount', kind=None),
                                                            Constant(value='livechat_visitor', kind=None),
                                                            Constant(value='members', kind=None),
                                                            Constant(value='message_needaction_counter', kind=None),
                                                            Constant(value='message_unread_counter', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='operator_pid', kind=None),
                                                            Constant(value='public', kind=None),
                                                            Constant(value='rtcSessions', kind=None),
                                                            Constant(value='seen_partners_info', kind=None),
                                                            Constant(value='seen_message_id', kind=None),
                                                            Constant(value='state', kind=None),
                                                            Constant(value='uuid', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='channel_livechat_1', ctx=Load()),
                                                                    attr='_get_avatar_cache_key',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            Constant(value='livechat', kind=None),
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
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_livechat_1', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
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
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=True, kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='channel_livechat_1', ctx=Load()),
                                                                                    attr='channel_last_seen_partner_ids',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='filtered',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Lambda(
                                                                                    args=arguments(
                                                                                        posonlyargs=[],
                                                                                        args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                                        vararg=None,
                                                                                        kwonlyargs=[],
                                                                                        kw_defaults=[],
                                                                                        kwarg=None,
                                                                                        defaults=[],
                                                                                    ),
                                                                                    body=Compare(
                                                                                        left=Attribute(
                                                                                            value=Name(id='p', ctx=Load()),
                                                                                            attr='partner_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[
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
                                                                                                attr='partner_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='last_interest_dt',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='strftime',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='DEFAULT_SERVER_DATETIME_FORMAT', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Name(id='next', ctx=Load()),
                                                                args=[
                                                                    GeneratorExp(
                                                                        elt=Subscript(
                                                                            value=Name(id='res', ctx=Load()),
                                                                            slice=Constant(value='message_id', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='res', ctx=Store()),
                                                                                iter=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='channel_livechat_1', ctx=Load()),
                                                                                        attr='_channel_last_message_ids',
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
                                                            Constant(value=2, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='country', kind=None),
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='name', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value=False, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Subscript(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='users',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                slice=Constant(value=1, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='partner_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='test1', kind=None),
                                                                ],
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='active', kind=None),
                                                                            Constant(value='display_name', kind=None),
                                                                            Constant(value='email', kind=None),
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='im_status', kind=None),
                                                                            Constant(value='is_internal_user', kind=None),
                                                                            Constant(value='name', kind=None),
                                                                            Constant(value='out_of_office_date_end', kind=None),
                                                                            Constant(value='user_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=True, kind=None),
                                                                            Constant(value='Ernest Employee', kind=None),
                                                                            Constant(value='e.e@example.com', kind=None),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='users',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='leave_offline', kind=None),
                                                                            Constant(value=True, kind=None),
                                                                            Constant(value='Ernest Employee', kind=None),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Call(
                                                                                            func=Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='leaves',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='filtered',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[
                                                                                                Lambda(
                                                                                                    args=arguments(
                                                                                                        posonlyargs=[],
                                                                                                        args=[arg(arg='l', annotation=None, type_comment=None)],
                                                                                                        vararg=None,
                                                                                                        kwonlyargs=[],
                                                                                                        kw_defaults=[],
                                                                                                        kwarg=None,
                                                                                                        defaults=[],
                                                                                                    ),
                                                                                                    body=Compare(
                                                                                                        left=Attribute(
                                                                                                            value=Attribute(
                                                                                                                value=Name(id='l', ctx=Load()),
                                                                                                                attr='employee_id',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            attr='user_id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        ops=[Eq()],
                                                                                                        comparators=[
                                                                                                            Subscript(
                                                                                                                value=Attribute(
                                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                                    attr='users',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                slice=Constant(value=0, kind=None),
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                ),
                                                                                            ],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        attr='date_to',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='strftime',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='DEFAULT_SERVER_DATE_FORMAT', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
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
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='active', kind=None),
                                                                            Constant(value='display_name', kind=None),
                                                                            Constant(value='email', kind=None),
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='im_status', kind=None),
                                                                            Constant(value='is_internal_user', kind=None),
                                                                            Constant(value='name', kind=None),
                                                                            Constant(value='out_of_office_date_end', kind=None),
                                                                            Constant(value='user_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=True, kind=None),
                                                                            Constant(value='test1', kind=None),
                                                                            Constant(value='test1@example.com', kind=None),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='users',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value=1, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='leave_offline', kind=None),
                                                                            Constant(value=True, kind=None),
                                                                            Constant(value='test1', kind=None),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Call(
                                                                                            func=Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='leaves',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='filtered',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[
                                                                                                Lambda(
                                                                                                    args=arguments(
                                                                                                        posonlyargs=[],
                                                                                                        args=[arg(arg='l', annotation=None, type_comment=None)],
                                                                                                        vararg=None,
                                                                                                        kwonlyargs=[],
                                                                                                        kw_defaults=[],
                                                                                                        kwarg=None,
                                                                                                        defaults=[],
                                                                                                    ),
                                                                                                    body=Compare(
                                                                                                        left=Attribute(
                                                                                                            value=Attribute(
                                                                                                                value=Name(id='l', ctx=Load()),
                                                                                                                attr='employee_id',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            attr='user_id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        ops=[Eq()],
                                                                                                        comparators=[
                                                                                                            Subscript(
                                                                                                                value=Attribute(
                                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                                    attr='users',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                slice=Constant(value=1, kind=None),
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                ),
                                                                                            ],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        attr='date_to',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='strftime',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='DEFAULT_SERVER_DATE_FORMAT', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
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
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='test1 Ernest Employee', kind=None),
                                                            Tuple(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Subscript(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='users',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                slice=Constant(value=0, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='partner_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='Ernest Employee', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='private', kind=None),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
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
                                                                            Constant(value='fetched_message_id', kind=None),
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='seen_message_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=False, kind=None),
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='channel_livechat_1', ctx=Load()),
                                                                                            attr='channel_last_seen_partner_ids',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='filtered',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[
                                                                                        Lambda(
                                                                                            args=arguments(
                                                                                                posonlyargs=[],
                                                                                                args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                                                vararg=None,
                                                                                                kwonlyargs=[],
                                                                                                kw_defaults=[],
                                                                                                kwarg=None,
                                                                                                defaults=[],
                                                                                            ),
                                                                                            body=Compare(
                                                                                                left=Attribute(
                                                                                                    value=Name(id='p', ctx=Load()),
                                                                                                    attr='partner_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[Eq()],
                                                                                                comparators=[
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
                                                                                                        attr='partner_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='users',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='fetched_message_id', kind=None),
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='seen_message_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Call(
                                                                                func=Name(id='next', ctx=Load()),
                                                                                args=[
                                                                                    GeneratorExp(
                                                                                        elt=Subscript(
                                                                                            value=Name(id='res', ctx=Load()),
                                                                                            slice=Constant(value='message_id', kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        generators=[
                                                                                            comprehension(
                                                                                                target=Name(id='res', ctx=Store()),
                                                                                                iter=Call(
                                                                                                    func=Attribute(
                                                                                                        value=Name(id='channel_livechat_1', ctx=Load()),
                                                                                                        attr='_channel_last_message_ids',
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
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='channel_livechat_1', ctx=Load()),
                                                                                            attr='channel_last_seen_partner_ids',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='filtered',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[
                                                                                        Lambda(
                                                                                            args=arguments(
                                                                                                posonlyargs=[],
                                                                                                args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                                                vararg=None,
                                                                                                kwonlyargs=[],
                                                                                                kw_defaults=[],
                                                                                                kwarg=None,
                                                                                                defaults=[],
                                                                                            ),
                                                                                            body=Compare(
                                                                                                left=Attribute(
                                                                                                    value=Name(id='p', ctx=Load()),
                                                                                                    attr='partner_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[Eq()],
                                                                                                comparators=[
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
                                                                                                        attr='partner_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='users',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value=1, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Call(
                                                                                func=Name(id='next', ctx=Load()),
                                                                                args=[
                                                                                    GeneratorExp(
                                                                                        elt=Subscript(
                                                                                            value=Name(id='res', ctx=Load()),
                                                                                            slice=Constant(value='message_id', kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        generators=[
                                                                                            comprehension(
                                                                                                target=Name(id='res', ctx=Store()),
                                                                                                iter=Call(
                                                                                                    func=Attribute(
                                                                                                        value=Name(id='channel_livechat_1', ctx=Load()),
                                                                                                        attr='_channel_last_message_ids',
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
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value='open', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_livechat_1', ctx=Load()),
                                                                attr='uuid',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='avatarCacheKey', kind=None),
                                                            Constant(value='channel_type', kind=None),
                                                            Constant(value='create_uid', kind=None),
                                                            Constant(value='custom_channel_name', kind=None),
                                                            Constant(value='defaultDisplayMode', kind=None),
                                                            Constant(value='description', kind=None),
                                                            Constant(value='group_based_subscription', kind=None),
                                                            Constant(value='id', kind=None),
                                                            Constant(value='invitedGuests', kind=None),
                                                            Constant(value='invitedPartners', kind=None),
                                                            Constant(value='is_minimized', kind=None),
                                                            Constant(value='is_pinned', kind=None),
                                                            Constant(value='last_interest_dt', kind=None),
                                                            Constant(value='last_message_id', kind=None),
                                                            Constant(value='memberCount', kind=None),
                                                            Constant(value='livechat_visitor', kind=None),
                                                            Constant(value='members', kind=None),
                                                            Constant(value='message_needaction_counter', kind=None),
                                                            Constant(value='message_unread_counter', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='operator_pid', kind=None),
                                                            Constant(value='public', kind=None),
                                                            Constant(value='rtcSessions', kind=None),
                                                            Constant(value='seen_partners_info', kind=None),
                                                            Constant(value='seen_message_id', kind=None),
                                                            Constant(value='state', kind=None),
                                                            Constant(value='uuid', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='channel_livechat_2', ctx=Load()),
                                                                    attr='_get_avatar_cache_key',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            Constant(value='livechat', kind=None),
                                                            Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='ref',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='base.public_user', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_livechat_2', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
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
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=True, kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='channel_livechat_2', ctx=Load()),
                                                                                    attr='channel_last_seen_partner_ids',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='filtered',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Lambda(
                                                                                    args=arguments(
                                                                                        posonlyargs=[],
                                                                                        args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                                        vararg=None,
                                                                                        kwonlyargs=[],
                                                                                        kw_defaults=[],
                                                                                        kwarg=None,
                                                                                        defaults=[],
                                                                                    ),
                                                                                    body=Compare(
                                                                                        left=Attribute(
                                                                                            value=Name(id='p', ctx=Load()),
                                                                                            attr='partner_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[
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
                                                                                                attr='partner_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='last_interest_dt',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='strftime',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='DEFAULT_SERVER_DATETIME_FORMAT', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Name(id='next', ctx=Load()),
                                                                args=[
                                                                    GeneratorExp(
                                                                        elt=Subscript(
                                                                            value=Name(id='res', ctx=Load()),
                                                                            slice=Constant(value='message_id', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='res', ctx=Store()),
                                                                                iter=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='channel_livechat_2', ctx=Load()),
                                                                                        attr='_channel_last_message_ids',
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
                                                            Constant(value=2, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='country', kind=None),
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='name', kind=None),
                                                                ],
                                                                values=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='env',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='ref',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[Constant(value='base.be', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='Belgium', kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=False, kind=None),
                                                                    Constant(value='anon 2', kind=None),
                                                                ],
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='active', kind=None),
                                                                            Constant(value='display_name', kind=None),
                                                                            Constant(value='email', kind=None),
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='im_status', kind=None),
                                                                            Constant(value='is_internal_user', kind=None),
                                                                            Constant(value='name', kind=None),
                                                                            Constant(value='out_of_office_date_end', kind=None),
                                                                            Constant(value='user_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value='Public user', kind=None),
                                                                            Constant(value=False, kind=None),
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='env',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='ref',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[Constant(value='base.public_partner', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='im_partner', kind=None),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value='Public user', kind=None),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=False, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='active', kind=None),
                                                                            Constant(value='display_name', kind=None),
                                                                            Constant(value='email', kind=None),
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='im_status', kind=None),
                                                                            Constant(value='is_internal_user', kind=None),
                                                                            Constant(value='name', kind=None),
                                                                            Constant(value='out_of_office_date_end', kind=None),
                                                                            Constant(value='user_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=True, kind=None),
                                                                            Constant(value='Ernest Employee', kind=None),
                                                                            Constant(value='e.e@example.com', kind=None),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='users',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='leave_offline', kind=None),
                                                                            Constant(value=True, kind=None),
                                                                            Constant(value='Ernest Employee', kind=None),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Call(
                                                                                            func=Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='leaves',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='filtered',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[
                                                                                                Lambda(
                                                                                                    args=arguments(
                                                                                                        posonlyargs=[],
                                                                                                        args=[arg(arg='l', annotation=None, type_comment=None)],
                                                                                                        vararg=None,
                                                                                                        kwonlyargs=[],
                                                                                                        kw_defaults=[],
                                                                                                        kwarg=None,
                                                                                                        defaults=[],
                                                                                                    ),
                                                                                                    body=Compare(
                                                                                                        left=Attribute(
                                                                                                            value=Attribute(
                                                                                                                value=Name(id='l', ctx=Load()),
                                                                                                                attr='employee_id',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            attr='user_id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        ops=[Eq()],
                                                                                                        comparators=[
                                                                                                            Subscript(
                                                                                                                value=Attribute(
                                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                                    attr='users',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                slice=Constant(value=0, kind=None),
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                ),
                                                                                            ],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        attr='date_to',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='strftime',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='DEFAULT_SERVER_DATE_FORMAT', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
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
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='anon 2 Ernest Employee', kind=None),
                                                            Tuple(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Subscript(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='users',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                slice=Constant(value=0, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='partner_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='Ernest Employee', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='private', kind=None),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='insert', kind=None),
                                                                            List(elts=[], ctx=Load()),
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
                                                                            Constant(value='fetched_message_id', kind=None),
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='seen_message_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Call(
                                                                                func=Name(id='next', ctx=Load()),
                                                                                args=[
                                                                                    GeneratorExp(
                                                                                        elt=Subscript(
                                                                                            value=Name(id='res', ctx=Load()),
                                                                                            slice=Constant(value='message_id', kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        generators=[
                                                                                            comprehension(
                                                                                                target=Name(id='res', ctx=Store()),
                                                                                                iter=Call(
                                                                                                    func=Attribute(
                                                                                                        value=Name(id='channel_livechat_2', ctx=Load()),
                                                                                                        attr='_channel_last_message_ids',
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
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='channel_livechat_2', ctx=Load()),
                                                                                            attr='channel_last_seen_partner_ids',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='filtered',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[
                                                                                        Lambda(
                                                                                            args=arguments(
                                                                                                posonlyargs=[],
                                                                                                args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                                                vararg=None,
                                                                                                kwonlyargs=[],
                                                                                                kw_defaults=[],
                                                                                                kwarg=None,
                                                                                                defaults=[],
                                                                                            ),
                                                                                            body=Compare(
                                                                                                left=Attribute(
                                                                                                    value=Name(id='p', ctx=Load()),
                                                                                                    attr='partner_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[Eq()],
                                                                                                comparators=[
                                                                                                    Call(
                                                                                                        func=Attribute(
                                                                                                            value=Attribute(
                                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                                attr='env',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            attr='ref',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        args=[Constant(value='base.public_partner', kind=None)],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='env',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='ref',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='base.public_user', kind=None)],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Call(
                                                                                func=Name(id='next', ctx=Load()),
                                                                                args=[
                                                                                    GeneratorExp(
                                                                                        elt=Subscript(
                                                                                            value=Name(id='res', ctx=Load()),
                                                                                            slice=Constant(value='message_id', kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        generators=[
                                                                                            comprehension(
                                                                                                target=Name(id='res', ctx=Store()),
                                                                                                iter=Call(
                                                                                                    func=Attribute(
                                                                                                        value=Name(id='channel_livechat_2', ctx=Load()),
                                                                                                        attr='_channel_last_message_ids',
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
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='fetched_message_id', kind=None),
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='seen_message_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value=False, kind=None),
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='channel_livechat_2', ctx=Load()),
                                                                                            attr='channel_last_seen_partner_ids',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='filtered',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[
                                                                                        Lambda(
                                                                                            args=arguments(
                                                                                                posonlyargs=[],
                                                                                                args=[arg(arg='p', annotation=None, type_comment=None)],
                                                                                                vararg=None,
                                                                                                kwonlyargs=[],
                                                                                                kw_defaults=[],
                                                                                                kwarg=None,
                                                                                                defaults=[],
                                                                                            ),
                                                                                            body=Compare(
                                                                                                left=Attribute(
                                                                                                    value=Name(id='p', ctx=Load()),
                                                                                                    attr='partner_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[Eq()],
                                                                                                comparators=[
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
                                                                                                        attr='partner_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='users',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='partner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value='open', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel_livechat_2', ctx=Load()),
                                                                attr='uuid',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='YourCompany', kind=None),
                                            List(elts=[], ctx=Load()),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='description', kind=None),
                                                            Constant(value='id', kind=None),
                                                            Constant(value='source', kind=None),
                                                            Constant(value='substitution', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value=False, kind=None),
                                                            Constant(value=1, kind=None),
                                                            Constant(value='hello', kind=None),
                                                            Constant(value='Hello. How may I help you?', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='description', kind=None),
                                                            Constant(value='id', kind=None),
                                                            Constant(value='source', kind=None),
                                                            Constant(value='substitution', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value=False, kind=None),
                                                            Constant(value=2, kind=None),
                                                            Constant(value='bye', kind=None),
                                                            Constant(value='Thanks for your feedback. Good bye!', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ir.model.data', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_xmlid_to_res_id',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='mail.menu_root_discuss', kind=None)],
                                                keywords=[],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='active', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='email', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='im_status', kind=None),
                                                    Constant(value='is_internal_user', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='out_of_office_date_end', kind=None),
                                                    Constant(value='user_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value='OdooBot', kind=None),
                                                    Constant(value='odoobot@example.com', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='user_root', ctx=Load()),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='bot', kind=None),
                                                    Constant(value=True, kind=None),
                                                    Constant(value='OdooBot', kind=None),
                                                    Constant(value=False, kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='active', kind=None),
                                                            Constant(value='display_name', kind=None),
                                                            Constant(value='email', kind=None),
                                                            Constant(value='id', kind=None),
                                                            Constant(value='im_status', kind=None),
                                                            Constant(value='is_internal_user', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='out_of_office_date_end', kind=None),
                                                            Constant(value='user_id', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value=False, kind=None),
                                                            Constant(value='Public user', kind=None),
                                                            Constant(value=False, kind=None),
                                                            Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='ref',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='base.public_partner', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='im_partner', kind=None),
                                                            Constant(value=False, kind=None),
                                                            Constant(value='Public user', kind=None),
                                                            Constant(value=False, kind=None),
                                                            Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='ref',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='base.public_user', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='active', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='email', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='im_status', kind=None),
                                                    Constant(value='is_internal_user', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='out_of_office_date_end', kind=None),
                                                    Constant(value='user_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=True, kind=None),
                                                    Constant(value='Ernest Employee', kind=None),
                                                    Constant(value='e.e@example.com', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='users',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='leave_offline', kind=None),
                                                    Constant(value=True, kind=None),
                                                    Constant(value='Ernest Employee', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='leaves',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='filtered',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Lambda(
                                                                            args=arguments(
                                                                                posonlyargs=[],
                                                                                args=[arg(arg='l', annotation=None, type_comment=None)],
                                                                                vararg=None,
                                                                                kwonlyargs=[],
                                                                                kw_defaults=[],
                                                                                kwarg=None,
                                                                                defaults=[],
                                                                            ),
                                                                            body=Compare(
                                                                                left=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='l', ctx=Load()),
                                                                                        attr='employee_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='user_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[
                                                                                    Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='users',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                attr='date_to',
                                                                ctx=Load(),
                                                            ),
                                                            attr='strftime',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='DEFAULT_SERVER_DATE_FORMAT', ctx=Load())],
                                                        keywords=[],
                                                    ),
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
                                            ),
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
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='is_discuss_sidebar_category_channel_open', kind=None),
                                                    Constant(value='is_discuss_sidebar_category_chat_open', kind=None),
                                                    Constant(value='is_discuss_sidebar_category_livechat_open', kind=None),
                                                    Constant(value='push_to_talk_key', kind=None),
                                                    Constant(value='use_push_to_talk', kind=None),
                                                    Constant(value='user_id', kind=None),
                                                    Constant(value='voice_active_duration', kind=None),
                                                    Constant(value='volume_settings', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='res.users.settings', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='_find_or_create_for_user',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='users',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=True, kind=None),
                                                    Constant(value=True, kind=None),
                                                    Constant(value=True, kind=None),
                                                    Constant(value=False, kind=None),
                                                    Constant(value=False, kind=None),
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
                                                            Constant(value='Ernest Employee', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=0, kind=None),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='emp', kind=None)],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
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
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
