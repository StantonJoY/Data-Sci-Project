Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='http', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.portal.controllers.portal',
            names=[
                alias(name='CustomerPortal', asname=None),
                alias(name='pager', asname='portal_pager'),
            ],
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
            module='collections',
            names=[alias(name='OrderedDict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ClassDef(
            name='PortalAccount',
            bases=[Name(id='CustomerPortal', ctx=Load())],
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
                        If(
                            test=Compare(
                                left=Constant(value='invoice_count', kind=None),
                                ops=[In()],
                                comparators=[Name(id='counters', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='invoice_count', ctx=Store())],
                                    value=IfExp(
                                        test=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='account.move', kind=None),
                                                    ctx=Load(),
                                                ),
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
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='account.move', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='search_count',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_get_invoices_domain',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        orelse=Constant(value=0, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='invoice_count', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='invoice_count', ctx=Load()),
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
                    name='_invoice_get_page_view_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='invoice', annotation=None, type_comment=None),
                            arg(arg='access_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='page_name', kind=None),
                                    Constant(value='invoice', kind=None),
                                ],
                                values=[
                                    Constant(value='invoice', kind=None),
                                    Name(id='invoice', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_page_view_values',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='invoice', ctx=Load()),
                                    Name(id='access_token', ctx=Load()),
                                    Name(id='values', ctx=Load()),
                                    Constant(value='my_invoices_history', kind=None),
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
                    name='_get_invoices_domain',
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
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='move_type', kind=None),
                                            Constant(value='in', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='out_invoice', kind=None),
                                                    Constant(value='out_refund', kind=None),
                                                    Constant(value='in_invoice', kind=None),
                                                    Constant(value='in_refund', kind=None),
                                                    Constant(value='out_receipt', kind=None),
                                                    Constant(value='in_receipt', kind=None),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='portal_my_invoices',
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
                            targets=[Name(id='AccountInvoice', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='account.move', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_invoices_domain',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='searchbar_sortings', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='date', kind=None),
                                    Constant(value='duedate', kind=None),
                                    Constant(value='name', kind=None),
                                    Constant(value='state', kind=None),
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
                                                args=[Constant(value='Date', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='invoice_date desc', kind=None),
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
                                                args=[Constant(value='Due Date', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='invoice_date_due desc', kind=None),
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
                                                args=[Constant(value='Reference', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='name desc', kind=None),
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
                                                args=[Constant(value='Status', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='state', kind=None),
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
                        Assign(
                            targets=[Name(id='searchbar_filters', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='all', kind=None),
                                    Constant(value='invoices', kind=None),
                                    Constant(value='bills', kind=None),
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
                                            List(elts=[], ctx=Load()),
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
                                                args=[Constant(value='Invoices', kind=None)],
                                                keywords=[],
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='move_type', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='out_invoice', kind=None),
                                                                    Constant(value='out_refund', kind=None),
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
                                                args=[Constant(value='Bills', kind=None)],
                                                keywords=[],
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='move_type', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='in_invoice', kind=None),
                                                                    Constant(value='in_refund', kind=None),
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
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='filterby', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='filterby', ctx=Store())],
                                    value=Constant(value='all', kind=None),
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
                            targets=[Name(id='invoice_count', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='AccountInvoice', ctx=Load()),
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
                                        value=Constant(value='/my/invoices', kind=None),
                                    ),
                                    keyword(
                                        arg='url_args',
                                        value=Dict(
                                            keys=[
                                                Constant(value='date_begin', kind=None),
                                                Constant(value='date_end', kind=None),
                                                Constant(value='sortby', kind=None),
                                            ],
                                            values=[
                                                Name(id='date_begin', ctx=Load()),
                                                Name(id='date_end', ctx=Load()),
                                                Name(id='sortby', ctx=Load()),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='total',
                                        value=Name(id='invoice_count', ctx=Load()),
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
                            targets=[Name(id='invoices', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='AccountInvoice', ctx=Load()),
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
                                    slice=Constant(value='my_invoices_history', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='invoices', ctx=Load()),
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
                                            Constant(value='invoices', kind=None),
                                            Constant(value='page_name', kind=None),
                                            Constant(value='pager', kind=None),
                                            Constant(value='default_url', kind=None),
                                            Constant(value='searchbar_sortings', kind=None),
                                            Constant(value='sortby', kind=None),
                                            Constant(value='searchbar_filters', kind=None),
                                            Constant(value='filterby', kind=None),
                                        ],
                                        values=[
                                            Name(id='date_begin', ctx=Load()),
                                            Name(id='invoices', ctx=Load()),
                                            Constant(value='invoice', kind=None),
                                            Name(id='pager', ctx=Load()),
                                            Constant(value='/my/invoices', kind=None),
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
                                    Constant(value='account.portal_my_invoices', kind=None),
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
                                    elts=[
                                        Constant(value='/my/invoices', kind=None),
                                        Constant(value='/my/invoices/page/<int:page>', kind=None),
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
                    name='portal_my_invoice_detail',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='invoice_id', annotation=None, type_comment=None),
                            arg(arg='access_token', annotation=None, type_comment=None),
                            arg(arg='report_type', annotation=None, type_comment=None),
                            arg(arg='download', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='invoice_sudo', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_document_check_access',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='account.move', kind=None),
                                            Name(id='invoice_id', ctx=Load()),
                                            Name(id='access_token', ctx=Load()),
                                        ],
                                        keywords=[],
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
                                                value=Name(id='invoice_sudo', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='report_type',
                                                value=Name(id='report_type', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='report_ref',
                                                value=Constant(value='account.account_invoices', kind=None),
                                            ),
                                            keyword(
                                                arg='download',
                                                value=Name(id='download', ctx=Load()),
                                            ),
                                        ],
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
                                    attr='_invoice_get_page_view_values',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='invoice_sudo', ctx=Load()),
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account.portal_invoice_page', kind=None),
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
                                    elts=[Constant(value='/my/invoices/<int:invoice_id>', kind=None)],
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
                    name='details_form_validate',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='error', ctx=Store()),
                                        Name(id='error_message', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='PortalAccount', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='details_form_validate',
                                    ctx=Load(),
                                ),
                                args=[Name(id='data', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partner', ctx=Store())],
                            value=Attribute(
                                value=Call(
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
                                    args=[
                                        Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='uid',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='partner_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='can_edit_vat',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Constant(value='vat', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='data', ctx=Load())],
                                            ),
                                            Compare(
                                                left=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Subscript(
                                                            value=Name(id='data', ctx=Load()),
                                                            slice=Constant(value='vat', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        Constant(value=False, kind=None),
                                                    ],
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='partner', ctx=Load()),
                                                                attr='vat',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='error', ctx=Load()),
                                                    slice=Constant(value='vat', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='error', kind=None),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='error_message', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Changing VAT number is not allowed once invoices have been issued for your account. Please contact us directly for this operation.', kind=None)],
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
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Constant(value='name', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='data', ctx=Load())],
                                            ),
                                            Compare(
                                                left=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Subscript(
                                                            value=Name(id='data', ctx=Load()),
                                                            slice=Constant(value='name', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        Constant(value=False, kind=None),
                                                    ],
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='partner', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='error', ctx=Load()),
                                                    slice=Constant(value='name', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='error', kind=None),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='error_message', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Changing your name is not allowed once invoices have been issued for your account. Please contact us directly for this operation.', kind=None)],
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
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Constant(value='company_name', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='data', ctx=Load())],
                                            ),
                                            Compare(
                                                left=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Subscript(
                                                            value=Name(id='data', ctx=Load()),
                                                            slice=Constant(value='company_name', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        Constant(value=False, kind=None),
                                                    ],
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='partner', ctx=Load()),
                                                                attr='company_name',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='error', ctx=Load()),
                                                    slice=Constant(value='company_name', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='error', kind=None),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='error_message', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Changing your company name is not allowed once invoices have been issued for your account. Please contact us directly for this operation.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='error', ctx=Load()),
                                    Name(id='error_message', ctx=Load()),
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
