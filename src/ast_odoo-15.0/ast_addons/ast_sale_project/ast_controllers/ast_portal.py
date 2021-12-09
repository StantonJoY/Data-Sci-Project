Module(
    body=[
        ImportFrom(
            module='operator',
            names=[alias(name='itemgetter', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='_', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='groupby', asname='groupbyelem')],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv.expression',
            names=[alias(name='OR', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.project.controllers.portal',
            names=[alias(name='ProjectCustomerPortal', asname=None)],
            level=0,
        ),
        ClassDef(
            name='SaleProjectCustomerPortal',
            bases=[Name(id='ProjectCustomerPortal', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='_task_get_searchbar_groupby',
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
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_task_get_searchbar_groupby',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='sale_order', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='input', kind=None),
                                    Constant(value='label', kind=None),
                                    Constant(value='order', kind=None),
                                ],
                                values=[
                                    Constant(value='sale_order', kind=None),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Sales Order', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value=7, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='sale_line', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='input', kind=None),
                                    Constant(value='label', kind=None),
                                    Constant(value='order', kind=None),
                                ],
                                values=[
                                    Constant(value='sale_line', kind=None),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Sales Order Item', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value=8, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='sorted', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='items',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='key',
                                                value=Lambda(
                                                    args=arguments(
                                                        posonlyargs=[],
                                                        args=[arg(arg='item', annotation=None, type_comment=None)],
                                                        vararg=None,
                                                        kwonlyargs=[],
                                                        kw_defaults=[],
                                                        kwarg=None,
                                                        defaults=[],
                                                    ),
                                                    body=Subscript(
                                                        value=Subscript(
                                                            value=Name(id='item', ctx=Load()),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='order', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ),
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
                    name='_task_get_groupby_mapping',
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
                                    attr='_task_get_groupby_mapping',
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
                                        arg='sale_order',
                                        value=Constant(value='sale_order_id', kind=None),
                                    ),
                                    keyword(
                                        arg='sale_line',
                                        value=Constant(value='sale_line_id', kind=None),
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
                    name='_task_get_searchbar_inputs',
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
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_task_get_searchbar_inputs',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='sale_order', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='input', kind=None),
                                    Constant(value='label', kind=None),
                                    Constant(value='order', kind=None),
                                ],
                                values=[
                                    Constant(value='sale_order', kind=None),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Search in Sales Order', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value=7, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='sale_line', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='input', kind=None),
                                    Constant(value='label', kind=None),
                                    Constant(value='order', kind=None),
                                ],
                                values=[
                                    Constant(value='sale_line', kind=None),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Search in Sales Order Item', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value=8, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='invoice', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='input', kind=None),
                                    Constant(value='label', kind=None),
                                    Constant(value='order', kind=None),
                                ],
                                values=[
                                    Constant(value='invoice', kind=None),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Search in Invoice', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value=9, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='sorted', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='items',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='key',
                                                value=Lambda(
                                                    args=arguments(
                                                        posonlyargs=[],
                                                        args=[arg(arg='item', annotation=None, type_comment=None)],
                                                        vararg=None,
                                                        kwonlyargs=[],
                                                        kw_defaults=[],
                                                        kwarg=None,
                                                        defaults=[],
                                                    ),
                                                    body=Subscript(
                                                        value=Subscript(
                                                            value=Name(id='item', ctx=Load()),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='order', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ),
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
                    name='_task_get_search_domain',
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
                            value=List(
                                elts=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='_task_get_search_domain',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='search_in', ctx=Load()),
                                            Name(id='search', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
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
                                            Constant(value='sale_order', kind=None),
                                            Constant(value='all', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='search_domain', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='sale_order_id.name', kind=None),
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
                                            Constant(value='sale_line', kind=None),
                                            Constant(value='all', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='search_domain', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='sale_line_id.name', kind=None),
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='search_domain', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='sale_order_id.invoice_ids.name', kind=None),
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
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='OR', ctx=Load()),
                                args=[Name(id='search_domain', ctx=Load())],
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
