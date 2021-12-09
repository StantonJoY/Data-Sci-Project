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
            module='odoo.exceptions',
            names=[
                alias(name='AccessError', asname=None),
                alias(name='MissingError', asname=None),
            ],
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
            module='odoo.addons.account.controllers',
            names=[alias(name='portal', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.hr_timesheet.controllers.portal',
            names=[alias(name='TimesheetCustomerPortal', asname=None)],
            level=0,
        ),
        ClassDef(
            name='PortalAccount',
            bases=[
                Attribute(
                    value=Name(id='portal', ctx=Load()),
                    attr='PortalAccount',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
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
                                    attr='_invoice_get_page_view_values',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='invoice', ctx=Load()),
                                    Name(id='access_token', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.analytic.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_timesheet_get_portal_domain',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='expression', ctx=Load()),
                                    attr='AND',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Name(id='domain', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='account.analytic.line', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_timesheet_get_sale_domain',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='invoice', ctx=Load()),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='line_ids.sale_line_ids', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
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
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Name(id='invoice', ctx=Load()),
                                                                        attr='id',
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
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='timesheets', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.analytic.line', kind=None),
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
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='is_uom_day', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.analytic.line', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_is_timesheet_encode_uom_day',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='SaleTimesheetCustomerPortal',
            bases=[Name(id='TimesheetCustomerPortal', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='_get_searchbar_inputs',
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
                            targets=[Name(id='searchbar_inputs', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_searchbar_inputs',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='searchbar_inputs', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='so',
                                        value=Dict(
                                            keys=[
                                                Constant(value='input', kind=None),
                                                Constant(value='label', kind=None),
                                            ],
                                            values=[
                                                Constant(value='so', kind=None),
                                                Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Search in Sales Order', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='sol',
                                        value=Dict(
                                            keys=[
                                                Constant(value='input', kind=None),
                                                Constant(value='label', kind=None),
                                            ],
                                            values=[
                                                Constant(value='sol', kind=None),
                                                Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Search in Sales Order Item', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='invoice',
                                        value=Dict(
                                            keys=[
                                                Constant(value='input', kind=None),
                                                Constant(value='label', kind=None),
                                            ],
                                            values=[
                                                Constant(value='invoice', kind=None),
                                                Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Search in Invoice', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Name(id='searchbar_inputs', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_searchbar_groupby',
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
                            targets=[Name(id='searchbar_groupby', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_searchbar_groupby',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='searchbar_groupby', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='so',
                                        value=Dict(
                                            keys=[
                                                Constant(value='input', kind=None),
                                                Constant(value='label', kind=None),
                                            ],
                                            values=[
                                                Constant(value='so', kind=None),
                                                Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Sales Order', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='sol',
                                        value=Dict(
                                            keys=[
                                                Constant(value='input', kind=None),
                                                Constant(value='label', kind=None),
                                            ],
                                            values=[
                                                Constant(value='sol', kind=None),
                                                Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Sales Order Item', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='invoice',
                                        value=Dict(
                                            keys=[
                                                Constant(value='input', kind=None),
                                                Constant(value='label', kind=None),
                                            ],
                                            values=[
                                                Constant(value='invoice', kind=None),
                                                Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Invoice', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Name(id='searchbar_groupby', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_search_domain',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='search_in', annotation=None, type_comment=None),
                            arg(arg='search', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='search_domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_search_domain',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='search_in', ctx=Load()),
                                    Name(id='search', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='search_in', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='sol', kind=None),
                                            Constant(value='all', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='search_domain', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='expression', ctx=Load()),
                                            attr='OR',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Name(id='search_domain', ctx=Load()),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='so_line', kind=None),
                                                                    Constant(value='ilike', kind=None),
                                                                    Name(id='search', ctx=Load()),
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
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='search_in', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='so', kind=None),
                                            Constant(value='all', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='search_domain', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='expression', ctx=Load()),
                                            attr='OR',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Name(id='search_domain', ctx=Load()),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='so_line.order_id.name', kind=None),
                                                                    Constant(value='ilike', kind=None),
                                                                    Name(id='search', ctx=Load()),
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
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='search_in', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='invoice', kind=None),
                                            Constant(value='all', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='invoices', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
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
                                                            Constant(value='name', kind=None),
                                                            Constant(value='ilike', kind=None),
                                                            Name(id='search', ctx=Load()),
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
                                Assign(
                                    targets=[Name(id='domain', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.analytic.line', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_timesheet_get_sale_domain',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='invoices', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='invoice_line_ids.sale_line_ids', kind=None)],
                                                keywords=[],
                                            ),
                                            Name(id='invoices', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='search_domain', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='expression', ctx=Load()),
                                            attr='OR',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Name(id='search_domain', ctx=Load()),
                                                    Name(id='domain', ctx=Load()),
                                                ],
                                                ctx=Load(),
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
                            value=Name(id='search_domain', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_groupby_mapping',
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
                            targets=[Name(id='groupby_mapping', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_groupby_mapping',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='groupby_mapping', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='sol',
                                        value=Constant(value='so_line', kind=None),
                                    ),
                                    keyword(
                                        arg='so',
                                        value=Constant(value='order_id', kind=None),
                                    ),
                                    keyword(
                                        arg='invoice',
                                        value=Constant(value='timesheet_invoice_id', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Name(id='groupby_mapping', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_searchbar_sortings',
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
                            targets=[Name(id='searchbar_sortings', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_searchbar_sortings',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='searchbar_sortings', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='sol',
                                        value=Dict(
                                            keys=[
                                                Constant(value='label', kind=None),
                                                Constant(value='order', kind=None),
                                            ],
                                            values=[
                                                Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Sales Order Item', kind=None)],
                                                    keywords=[],
                                                ),
                                                Constant(value='so_line', kind=None),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Name(id='searchbar_sortings', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_task_get_page_view_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='task', annotation=None, type_comment=None),
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
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_task_get_page_view_values',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='task', ctx=Load()),
                                    Name(id='access_token', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='so_accessible', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='task', ctx=Load()),
                                                attr='sale_order_id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_document_check_access',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='sale.order', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='task', ctx=Load()),
                                                            attr='sale_order_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='so_accessible', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
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
                                    body=[Pass()],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='invoices_accessible', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='invoice', ctx=Store()),
                            iter=Attribute(
                                value=Attribute(
                                    value=Name(id='task', ctx=Load()),
                                    attr='sale_order_id',
                                    ctx=Load(),
                                ),
                                attr='invoice_ids',
                                ctx=Load(),
                            ),
                            body=[
                                Try(
                                    body=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_document_check_access',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='account.move', kind=None),
                                                    Attribute(
                                                        value=Name(id='invoice', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='values', ctx=Load()),
                                                                slice=Constant(value='invoices_accessible', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='invoice', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
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
                                            body=[Pass()],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
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
                    name='portal_my_timesheets',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='page', annotation=None, type_comment=None),
                            arg(arg='sortby', annotation=None, type_comment=None),
                            arg(arg='filterby', annotation=None, type_comment=None),
                            arg(arg='search', annotation=None, type_comment=None),
                            arg(arg='search_in', annotation=None, type_comment=None),
                            arg(arg='groupby', annotation=None, type_comment=None),
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
                            Constant(value='all', kind=None),
                            Constant(value='sol', kind=None),
                        ],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='portal_my_timesheets',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='page', ctx=Load()),
                                    Name(id='sortby', ctx=Load()),
                                    Name(id='filterby', ctx=Load()),
                                    Name(id='search', ctx=Load()),
                                    Name(id='search_in', ctx=Load()),
                                    Name(id='groupby', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kw', ctx=Load()),
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
                                    elts=[
                                        Constant(value='/my/timesheets', kind=None),
                                        Constant(value='/my/timesheets/page/<int:page>', kind=None),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
