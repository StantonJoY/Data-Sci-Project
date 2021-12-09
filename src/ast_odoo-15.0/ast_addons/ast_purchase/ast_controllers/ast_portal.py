Module(
    body=[
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        ImportFrom(
            module='collections',
            names=[alias(name='OrderedDict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='datetime',
            names=[alias(name='datetime', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='http', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[
                alias(name='AccessError', asname=None),
                alias(name='MissingError', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[
                alias(name='request', asname=None),
                alias(name='Response', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='image_process', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.translate',
            names=[alias(name='_', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.portal.controllers',
            names=[alias(name='portal', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.portal.controllers.portal',
            names=[alias(name='pager', asname='portal_pager')],
            level=0,
        ),
        ClassDef(
            name='CustomerPortal',
            bases=[
                Attribute(
                    value=Name(id='portal', ctx=Load()),
                    attr='CustomerPortal',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='_prepare_home_portal_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='counters', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_prepare_home_portal_values',
                                    ctx=Load(),
                                ),
                                args=[Name(id='counters', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='PurchaseOrder', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='purchase.order', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='rfq_count', kind=None),
                                ops=[In()],
                                comparators=[Name(id='counters', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='rfq_count', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=IfExp(
                                        test=Call(
                                            func=Attribute(
                                                value=Name(id='PurchaseOrder', ctx=Load()),
                                                attr='check_access_rights',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='read', kind=None)],
                                            keywords=[
                                                keyword(
                                                    arg='raise_exception',
                                                    value=Constant(value=False, kind=None),
                                                ),
                                            ],
                                        ),
                                        body=Call(
                                            func=Attribute(
                                                value=Name(id='PurchaseOrder', ctx=Load()),
                                                attr='search_count',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='state', kind=None),
                                                                Constant(value='in', kind=None),
                                                                List(
                                                                    elts=[Constant(value='sent', kind=None)],
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
                                        orelse=Constant(value=0, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='purchase_count', kind=None),
                                ops=[In()],
                                comparators=[Name(id='counters', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='purchase_count', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=IfExp(
                                        test=Call(
                                            func=Attribute(
                                                value=Name(id='PurchaseOrder', ctx=Load()),
                                                attr='check_access_rights',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='read', kind=None)],
                                            keywords=[
                                                keyword(
                                                    arg='raise_exception',
                                                    value=Constant(value=False, kind=None),
                                                ),
                                            ],
                                        ),
                                        body=Call(
                                            func=Attribute(
                                                value=Name(id='PurchaseOrder', ctx=Load()),
                                                attr='search_count',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='state', kind=None),
                                                                Constant(value='in', kind=None),
                                                                List(
                                                                    elts=[
                                                                        Constant(value='purchase', kind=None),
                                                                        Constant(value='done', kind=None),
                                                                        Constant(value='cancel', kind=None),
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
                                        orelse=Constant(value=0, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_render_portal',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='template', annotation=None, type_comment=None),
                            arg(arg='page', annotation=None, type_comment=None),
                            arg(arg='date_begin', annotation=None, type_comment=None),
                            arg(arg='date_end', annotation=None, type_comment=None),
                            arg(arg='sortby', annotation=None, type_comment=None),
                            arg(arg='filterby', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='searchbar_filters', annotation=None, type_comment=None),
                            arg(arg='default_filter', annotation=None, type_comment=None),
                            arg(arg='url', annotation=None, type_comment=None),
                            arg(arg='history', annotation=None, type_comment=None),
                            arg(arg='page_name', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_portal_layout_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='PurchaseOrder', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='purchase.order', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='date_begin', ctx=Load()),
                                    Name(id='date_end', ctx=Load()),
                                ],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='domain', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='create_date', kind=None),
                                                    Constant(value='>', kind=None),
                                                    Name(id='date_begin', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='create_date', kind=None),
                                                    Constant(value='<=', kind=None),
                                                    Name(id='date_end', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='searchbar_sortings', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='date', kind=None),
                                    Constant(value='name', kind=None),
                                    Constant(value='amount_total', kind=None),
                                ],
                                values=[
                                    Dict(
                                        keys=[
                                            Constant(value='label', kind=None),
                                            Constant(value='order', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Newest', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='create_date desc, id desc', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='label', kind=None),
                                            Constant(value='order', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Name', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='name asc, id asc', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='label', kind=None),
                                            Constant(value='order', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Total', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='amount_total desc, id desc', kind=None),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='sortby', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='sortby', ctx=Store())],
                                    value=Constant(value='date', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='order', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='searchbar_sortings', ctx=Load()),
                                    slice=Name(id='sortby', ctx=Load()),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='order', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='searchbar_filters', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='filterby', ctx=Load()),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='filterby', ctx=Store())],
                                            value=Name(id='default_filter', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                AugAssign(
                                    target=Name(id='domain', ctx=Store()),
                                    op=Add(),
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id='searchbar_filters', ctx=Load()),
                                            slice=Name(id='filterby', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='domain', kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='count', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='PurchaseOrder', ctx=Load()),
                                    attr='search_count',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pager', ctx=Store())],
                            value=Call(
                                func=Name(id='portal_pager', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='url',
                                        value=Name(id='url', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='url_args',
                                        value=Dict(
                                            keys=[
                                                Constant(value='date_begin', kind=None),
                                                Constant(value='date_end', kind=None),
                                                Constant(value='sortby', kind=None),
                                                Constant(value='filterby', kind=None),
                                            ],
                                            values=[
                                                Name(id='date_begin', ctx=Load()),
                                                Name(id='date_end', ctx=Load()),
                                                Name(id='sortby', ctx=Load()),
                                                Name(id='filterby', ctx=Load()),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='total',
                                        value=Name(id='count', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='page',
                                        value=Name(id='page', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='step',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_items_per_page',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='orders', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='PurchaseOrder', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Name(id='order', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_items_per_page',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='offset',
                                        value=Subscript(
                                            value=Name(id='pager', ctx=Load()),
                                            slice=Constant(value='offset', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='session',
                                        ctx=Load(),
                                    ),
                                    slice=Name(id='history', ctx=Load()),
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='orders', ctx=Load()),
                                    attr='ids',
                                    ctx=Load(),
                                ),
                                slice=Slice(
                                    lower=None,
                                    upper=Constant(value=100, kind=None),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='date', kind=None),
                                            Name(id='key', ctx=Load()),
                                            Constant(value='page_name', kind=None),
                                            Constant(value='pager', kind=None),
                                            Constant(value='searchbar_sortings', kind=None),
                                            Constant(value='sortby', kind=None),
                                            Constant(value='searchbar_filters', kind=None),
                                            Constant(value='filterby', kind=None),
                                            Constant(value='default_url', kind=None),
                                        ],
                                        values=[
                                            Name(id='date_begin', ctx=Load()),
                                            Name(id='orders', ctx=Load()),
                                            Name(id='page_name', ctx=Load()),
                                            Name(id='pager', ctx=Load()),
                                            Name(id='searchbar_sortings', ctx=Load()),
                                            Name(id='sortby', ctx=Load()),
                                            Call(
                                                func=Name(id='OrderedDict', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='sorted', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='searchbar_filters', ctx=Load()),
                                                                    attr='items',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='filterby', ctx=Load()),
                                            Name(id='url', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='template', ctx=Load()),
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
                FunctionDef(
                    name='_purchase_order_get_page_view_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='order', annotation=None, type_comment=None),
                            arg(arg='access_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        FunctionDef(
                            name='resize_to_48',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='b64source', annotation=None, type_comment=None)],
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
                                        operand=Name(id='b64source', ctx=Load()),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='b64source', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='base64', ctx=Load()),
                                                    attr='b64encode',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='ir.http', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='_placeholder',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Call(
                                        func=Name(id='image_process', ctx=Load()),
                                        args=[Name(id='b64source', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='size',
                                                value=Tuple(
                                                    elts=[
                                                        Constant(value=48, kind=None),
                                                        Constant(value=48, kind=None),
                                                    ],
                                                    ctx=Load(),
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
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='order', kind=None),
                                    Constant(value='resize_to_48', kind=None),
                                    Constant(value='report_type', kind=None),
                                ],
                                values=[
                                    Name(id='order', ctx=Load()),
                                    Name(id='resize_to_48', ctx=Load()),
                                    Constant(value='html', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='order', ctx=Load()),
                                    attr='state',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[Constant(value='sent', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='history', ctx=Store())],
                                    value=Constant(value='my_rfqs_history', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='history', ctx=Store())],
                                    value=Constant(value='my_purchases_history', kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_page_view_values',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='order', ctx=Load()),
                                    Name(id='access_token', ctx=Load()),
                                    Name(id='values', ctx=Load()),
                                    Name(id='history', ctx=Load()),
                                    Constant(value=False, kind=None),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='portal_my_requests_for_quotation',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='page', annotation=None, type_comment=None),
                            arg(arg='date_begin', annotation=None, type_comment=None),
                            arg(arg='date_end', annotation=None, type_comment=None),
                            arg(arg='sortby', annotation=None, type_comment=None),
                            arg(arg='filterby', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=1, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_render_portal',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='purchase.portal_my_purchase_rfqs', kind=None),
                                    Name(id='page', ctx=Load()),
                                    Name(id='date_begin', ctx=Load()),
                                    Name(id='date_end', ctx=Load()),
                                    Name(id='sortby', ctx=Load()),
                                    Name(id='filterby', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='state', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='sent', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(keys=[], values=[]),
                                    Constant(value=None, kind=None),
                                    Constant(value='/my/rfq', kind=None),
                                    Constant(value='my_rfqs_history', kind=None),
                                    Constant(value='rfq', kind=None),
                                    Constant(value='rfqs', kind=None),
                                ],
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
                            args=[
                                List(
                                    elts=[
                                        Constant(value='/my/rfq', kind=None),
                                        Constant(value='/my/rfq/page/<int:page>', kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='portal_my_purchase_orders',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='page', annotation=None, type_comment=None),
                            arg(arg='date_begin', annotation=None, type_comment=None),
                            arg(arg='date_end', annotation=None, type_comment=None),
                            arg(arg='sortby', annotation=None, type_comment=None),
                            arg(arg='filterby', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=1, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_render_portal',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='purchase.portal_my_purchase_orders', kind=None),
                                    Name(id='page', ctx=Load()),
                                    Name(id='date_begin', ctx=Load()),
                                    Name(id='date_end', ctx=Load()),
                                    Name(id='sortby', ctx=Load()),
                                    Name(id='filterby', ctx=Load()),
                                    List(elts=[], ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='all', kind=None),
                                            Constant(value='purchase', kind=None),
                                            Constant(value='cancel', kind=None),
                                            Constant(value='done', kind=None),
                                        ],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='label', kind=None),
                                                    Constant(value='domain', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='All', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='state', kind=None),
                                                                    Constant(value='in', kind=None),
                                                                    List(
                                                                        elts=[
                                                                            Constant(value='purchase', kind=None),
                                                                            Constant(value='done', kind=None),
                                                                            Constant(value='cancel', kind=None),
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
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='label', kind=None),
                                                    Constant(value='domain', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Purchase Order', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='state', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value='purchase', kind=None),
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
                                                    Constant(value='label', kind=None),
                                                    Constant(value='domain', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Cancelled', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='state', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value='cancel', kind=None),
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
                                                    Constant(value='label', kind=None),
                                                    Constant(value='domain', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Locked', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='state', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value='done', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Constant(value='all', kind=None),
                                    Constant(value='/my/purchase', kind=None),
                                    Constant(value='my_purchases_history', kind=None),
                                    Constant(value='purchase', kind=None),
                                    Constant(value='orders', kind=None),
                                ],
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
                            args=[
                                List(
                                    elts=[
                                        Constant(value='/my/purchase', kind=None),
                                        Constant(value='/my/purchase/page/<int:page>', kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='portal_my_purchase_order',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='order_id', annotation=None, type_comment=None),
                            arg(arg='access_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='order_sudo', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_document_check_access',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='purchase.order', kind=None),
                                            Name(id='order_id', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='access_token',
                                                value=Name(id='access_token', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Tuple(
                                        elts=[
                                            Name(id='AccessError', ctx=Load()),
                                            Name(id='MissingError', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='redirect',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='/my', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Assign(
                            targets=[Name(id='report_type', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kw', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='report_type', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='report_type', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='html', kind=None),
                                            Constant(value='pdf', kind=None),
                                            Constant(value='text', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_show_report',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='model',
                                                value=Name(id='order_sudo', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='report_type',
                                                value=Name(id='report_type', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='report_ref',
                                                value=Constant(value='purchase.action_report_purchase_order', kind=None),
                                            ),
                                            keyword(
                                                arg='download',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='kw', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='download', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='confirm_type', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kw', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='confirm', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='confirm_type', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='reminder', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='order_sudo', ctx=Load()),
                                            attr='confirm_reminder_mail',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='kw', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='confirmed_date', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='confirm_type', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='reception', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='order_sudo', ctx=Load()),
                                            attr='_confirm_reception_mail',
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
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_purchase_order_get_page_view_values',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='order_sudo', ctx=Load()),
                                    Name(id='access_token', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kw', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='update_date', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kw', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='update', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='order_sudo', ctx=Load()),
                                attr='company_id',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='res_company', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='order_sudo', ctx=Load()),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='update_date', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='True', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='render',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='purchase.portal_my_purchase_order_update_date', kind=None),
                                            Name(id='values', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='purchase.portal_my_purchase_order', kind=None),
                                    Name(id='values', ctx=Load()),
                                ],
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
                            args=[
                                List(
                                    elts=[Constant(value='/my/purchase/<int:order_id>', kind=None)],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='portal_my_purchase_order_update_dates',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='order_id', annotation=None, type_comment=None),
                            arg(arg='access_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='User update scheduled date on purchase order line.\n        ', kind=None),
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='order_sudo', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_document_check_access',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='purchase.order', kind=None),
                                            Name(id='order_id', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='access_token',
                                                value=Name(id='access_token', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Tuple(
                                        elts=[
                                            Name(id='AccessError', ctx=Load()),
                                            Name(id='MissingError', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='redirect',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='/my', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Assign(
                            targets=[Name(id='updated_dates', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='id_str', ctx=Store()),
                                    Name(id='date_str', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='kw', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='line_id', ctx=Store())],
                                            value=Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[Name(id='id_str', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='ValueError', ctx=Load()),
                                            name=None,
                                            body=[
                                                Return(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='redirect',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='order_sudo', ctx=Load()),
                                                                    attr='get_portal_url',
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
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                                Assign(
                                    targets=[Name(id='line', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='order_sudo', ctx=Load()),
                                                attr='order_line',
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
                                                        value=Name(id='l', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Name(id='line_id', ctx=Load())],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='line', ctx=Load()),
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='redirect',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='order_sudo', ctx=Load()),
                                                            attr='get_portal_url',
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
                                    orelse=[],
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='updated_date', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='_convert_to_middle_of_day',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='datetime', ctx=Load()),
                                                            attr='strptime',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='date_str', ctx=Load()),
                                                            Constant(value='%Y-%m-%d', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='ValueError', ctx=Load()),
                                            name=None,
                                            body=[Continue()],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='updated_dates', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Name(id='line', ctx=Load()),
                                                    Name(id='updated_date', ctx=Load()),
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
                        If(
                            test=Name(id='updated_dates', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='order_sudo', ctx=Load()),
                                            attr='_update_date_planned_for_lines',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='updated_dates', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='Response', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='status',
                                        value=Constant(value=204, kind=None),
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
                            args=[
                                List(
                                    elts=[Constant(value='/my/purchase/<int:order_id>/update', kind=None)],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
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
