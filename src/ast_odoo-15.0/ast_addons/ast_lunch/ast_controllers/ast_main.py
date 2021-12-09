Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='http', asname=None),
                alias(name='fields', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='AccessError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv',
            names=[alias(name='expression', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='float_round', asname=None),
                alias(name='float_repr', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='LunchController',
            bases=[
                Attribute(
                    value=Name(id='http', ctx=Load()),
                    attr='Controller',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='infos',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='user_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_user_impersonification',
                                    ctx=Load(),
                                ),
                                args=[Name(id='user_id', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='user', ctx=Store())],
                            value=IfExp(
                                test=Name(id='user_id', ctx=Load()),
                                body=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='res.users', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='browse',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='user_id', ctx=Load())],
                                    keywords=[],
                                ),
                                orelse=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='user',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='infos', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_make_infos',
                                    ctx=Load(),
                                ),
                                args=[Name(id='user', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_current_lines',
                                    ctx=Load(),
                                ),
                                args=[Name(id='user', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='lines', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='lines', ctx=Store())],
                                    value=ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='id', kind=None),
                                                Constant(value='product', kind=None),
                                                Constant(value='toppings', kind=None),
                                                Constant(value='quantity', kind=None),
                                                Constant(value='price', kind=None),
                                                Constant(value='state', kind=None),
                                                Constant(value='note', kind=None),
                                            ],
                                            values=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                        Call(
                                                            func=Name(id='float_repr', ctx=Load()),
                                                            args=[
                                                                Call(
                                                                    func=Name(id='float_round', ctx=Load()),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='line', ctx=Load()),
                                                                                attr='product_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='price',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Constant(value=2, kind=None),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                Constant(value=2, kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                ListComp(
                                                    elt=Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Name(id='topping', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Name(id='float_repr', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='float_round', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='topping', ctx=Load()),
                                                                                attr='price',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=2, kind=None),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    Constant(value=2, kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='topping', ctx=Store()),
                                                            iter=BinOp(
                                                                left=BinOp(
                                                                    left=Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='topping_ids_1',
                                                                        ctx=Load(),
                                                                    ),
                                                                    op=BitOr(),
                                                                    right=Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='topping_ids_2',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                                op=BitOr(),
                                                                right=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='topping_ids_3',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            ifs=[],
                                                            is_async=0,
                                                        ),
                                                    ],
                                                ),
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='quantity',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='price',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='state',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='note',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='line', ctx=Store()),
                                                iter=Name(id='lines', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='raw_state', ctx=Store()),
                                                Name(id='state', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_state',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='lines', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='infos', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='total', kind=None),
                                                    Constant(value='raw_state', kind=None),
                                                    Constant(value='state', kind=None),
                                                    Constant(value='lines', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='float_repr', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='float_round', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='sum', ctx=Load()),
                                                                        args=[
                                                                            GeneratorExp(
                                                                                elt=Subscript(
                                                                                    value=Name(id='line', ctx=Load()),
                                                                                    slice=Constant(value='price', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                generators=[
                                                                                    comprehension(
                                                                                        target=Name(id='line', ctx=Store()),
                                                                                        iter=Name(id='lines', ctx=Load()),
                                                                                        ifs=[],
                                                                                        is_async=0,
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    Constant(value=2, kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Constant(value=2, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Name(id='raw_state', ctx=Load()),
                                                    Name(id='state', ctx=Load()),
                                                    Name(id='lines', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='infos', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/lunch/infos', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='trash',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='user_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_user_impersonification',
                                    ctx=Load(),
                                ),
                                args=[Name(id='user_id', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='user', ctx=Store())],
                            value=IfExp(
                                test=Name(id='user_id', ctx=Load()),
                                body=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='res.users', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='browse',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='user_id', ctx=Load())],
                                    keywords=[],
                                ),
                                orelse=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='user',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_current_lines',
                                    ctx=Load(),
                                ),
                                args=[Name(id='user', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='lines', ctx=Load()),
                                    attr='action_cancel',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='lines', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/lunch/trash', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='pay',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='user_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_user_impersonification',
                                    ctx=Load(),
                                ),
                                args=[Name(id='user_id', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='user', ctx=Store())],
                            value=IfExp(
                                test=Name(id='user_id', ctx=Load()),
                                body=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='res.users', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='browse',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='user_id', ctx=Load())],
                                    keywords=[],
                                ),
                                orelse=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='user',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_current_lines',
                                    ctx=Load(),
                                ),
                                args=[Name(id='user', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='lines', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='lines', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='lines', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='line', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='state',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='new', kind=None)],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='lines', ctx=Load()),
                                            attr='action_order',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/lunch/pay', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='payment_message',
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
                                keys=[Constant(value='message', kind=None)],
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
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
                                            Constant(value='lunch.lunch_payment_dialog', kind=None),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/lunch/payment_message', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='set_user_location',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='location_id', annotation=None, type_comment=None),
                            arg(arg='user_id', annotation=None, type_comment=None),
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_user_impersonification',
                                    ctx=Load(),
                                ),
                                args=[Name(id='user_id', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='user', ctx=Store())],
                            value=IfExp(
                                test=Name(id='user_id', ctx=Load()),
                                body=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='res.users', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='browse',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='user_id', ctx=Load())],
                                    keywords=[],
                                ),
                                orelse=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='user',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='user', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='last_lunch_location_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='lunch.location', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='location_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/lunch/user_location_set', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_user_location',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='user_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_user_impersonification',
                                    ctx=Load(),
                                ),
                                args=[Name(id='user_id', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='user', ctx=Store())],
                            value=IfExp(
                                test=Name(id='user_id', ctx=Load()),
                                body=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='res.users', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='browse',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='user_id', ctx=Load())],
                                    keywords=[],
                                ),
                                orelse=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='user',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user_location', ctx=Store())],
                            value=Attribute(
                                value=Name(id='user', ctx=Load()),
                                attr='last_lunch_location_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='has_multi_company_access', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='user_location', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='user_location', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='_context',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='allowed_company_ids', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='company',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='user_location', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='has_multi_company_access', ctx=Load()),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='lunch.location', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='search',
                                                ctx=Load(),
                                            ),
                                            args=[List(elts=[], ctx=Load())],
                                            keywords=[
                                                keyword(
                                                    arg='limit',
                                                    value=Constant(value=1, kind=None),
                                                ),
                                            ],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='user_location', ctx=Load()),
                                attr='id',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/lunch/user_location_get', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_make_infos',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='user', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[Name(id='kwargs', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='is_manager', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                    attr='has_group',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='lunch.group_lunch_manager', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='currency', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='user', ctx=Load()),
                                    attr='company_id',
                                    ctx=Load(),
                                ),
                                attr='currency_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='res', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='username', kind=None),
                                            Constant(value='userimage', kind=None),
                                            Constant(value='wallet', kind=None),
                                            Constant(value='is_manager', kind=None),
                                            Constant(value='group_portal_id', kind=None),
                                            Constant(value='locations', kind=None),
                                            Constant(value='currency', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='user', ctx=Load()),
                                                        attr='sudo',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value='/web/image?model=res.users&id=%s&field=avatar_128', kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='user', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='lunch.cashmove', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='get_wallet_balance',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='user', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='is_manager', ctx=Load()),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ref',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='base.group_portal', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='lunch.location', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='search_read',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(elts=[], ctx=Load()),
                                                    List(
                                                        elts=[Constant(value='name', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='symbol', kind=None),
                                                    Constant(value='position', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='currency', ctx=Load()),
                                                        attr='symbol',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='currency', ctx=Load()),
                                                        attr='position',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='user_location', ctx=Store())],
                            value=Attribute(
                                value=Name(id='user', ctx=Load()),
                                attr='last_lunch_location_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='has_multi_company_access', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='user_location', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='user_location', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='_context',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='allowed_company_ids', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='company',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='user_location', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='has_multi_company_access', ctx=Load()),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='user', ctx=Load()),
                                            attr='last_lunch_location_id',
                                            ctx=Store(),
                                        ),
                                        Name(id='user_location', ctx=Store()),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='lunch.location', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='limit',
                                                value=Constant(value=1, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='alert_domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='expression', ctx=Load()),
                                    attr='AND',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
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
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='location_ids', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Attribute(
                                                                value=Name(id='user_location', ctx=Load()),
                                                                attr='id',
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
                                                            Constant(value='mode', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='alert', kind=None),
                                                        ],
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
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='res', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='user_location', kind=None),
                                            Constant(value='alerts', kind=None),
                                        ],
                                        values=[
                                            Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='user_location', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='user_location', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='lunch.alert', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='search_read',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='alert_domain', ctx=Load()),
                                                    List(
                                                        elts=[Constant(value='message', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_user_impersonification',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='user_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='user_id', ctx=Load()),
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='uid',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Name(id='user_id', ctx=Load())],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='has_group',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='lunch.group_lunch_manager', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='AccessError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='You are trying to impersonate another user, but this can only be done by a lunch manager', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_current_lines',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='user', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='lunch.order', kind=None),
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
                                                    Constant(value='user_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='user', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='date', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='Date',
                                                                ctx=Load(),
                                                            ),
                                                            attr='context_today',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='user', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='state', kind=None),
                                                    Constant(value='!=', kind=None),
                                                    Constant(value='cancelled', kind=None),
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
                    name='_get_state',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='lines', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n            This method returns the lowest state of the list of lines\n\n            eg: [confirmed, confirmed, new] will return ('new', 'To Order')\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='states_to_int', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='new', kind=None),
                                    Constant(value='ordered', kind=None),
                                    Constant(value='confirmed', kind=None),
                                    Constant(value='cancelled', kind=None),
                                ],
                                values=[
                                    Constant(value=0, kind=None),
                                    Constant(value=1, kind=None),
                                    Constant(value=2, kind=None),
                                    Constant(value=3, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='int_to_states', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='new', kind=None),
                                    Constant(value='ordered', kind=None),
                                    Constant(value='confirmed', kind=None),
                                    Constant(value='cancelled', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='translated_states', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='lunch.order', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_fields',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='state', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_description_selection',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='state', ctx=Store())],
                            value=Subscript(
                                value=Name(id='int_to_states', ctx=Load()),
                                slice=Call(
                                    func=Name(id='min', ctx=Load()),
                                    args=[
                                        GeneratorExp(
                                            elt=Subscript(
                                                value=Name(id='states_to_int', ctx=Load()),
                                                slice=Subscript(
                                                    value=Name(id='line', ctx=Load()),
                                                    slice=Constant(value='state', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            generators=[
                                                comprehension(
                                                    target=Name(id='line', ctx=Store()),
                                                    iter=Name(id='lines', ctx=Load()),
                                                    ifs=[],
                                                    is_async=0,
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='state', ctx=Load()),
                                    Subscript(
                                        value=Name(id='translated_states', ctx=Load()),
                                        slice=Name(id='state', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
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
