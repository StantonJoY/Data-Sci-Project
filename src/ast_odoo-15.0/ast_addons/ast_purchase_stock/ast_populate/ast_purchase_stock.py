Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='populate', asname=None),
                alias(name='groupby', asname=None),
            ],
            level=0,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='PurchaseOrder',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='purchase.order', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_populate_dependencies', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='res.partner', kind=None),
                            Constant(value='stock.picking.type', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_populate_factories',
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
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_populate_factories',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='picking_types', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.picking.type', kind=None),
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
                                                    Constant(value='code', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='incoming', kind=None),
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
                            targets=[Name(id='picking_types_by_company', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='groupby', ctx=Load()),
                                        args=[Name(id='picking_types', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='key',
                                                value=Lambda(
                                                    args=arguments(
                                                        posonlyargs=[],
                                                        args=[arg(arg='par', annotation=None, type_comment=None)],
                                                        vararg=None,
                                                        kwonlyargs=[],
                                                        kw_defaults=[],
                                                        kwarg=None,
                                                        defaults=[],
                                                    ),
                                                    body=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='par', ctx=Load()),
                                                            attr='company_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='picking_types_inter_company', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.picking.type', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='concat',
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='picking_types_by_company', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value=False, kind=None),
                                                List(elts=[], ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='picking_types_by_company', ctx=Store())],
                            value=DictComp(
                                key=Name(id='com', ctx=Load()),
                                value=BinOp(
                                    left=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='stock.picking.type', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='concat',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Starred(
                                                value=Name(id='pt', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    op=BitOr(),
                                    right=Name(id='picking_types_inter_company', ctx=Load()),
                                ),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='com', ctx=Store()),
                                                Name(id='pt', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='picking_types_by_company', ctx=Load()),
                                                attr='items',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ifs=[Name(id='com', ctx=Load())],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='get_picking_type_id',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='values', annotation=None, type_comment=None),
                                    arg(arg='random', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                                defaults=[
                                    Constant(value=None, kind=None),
                                    Constant(value=None, kind=None),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='random', ctx=Load()),
                                                attr='choice',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Subscript(
                                                    value=Name(id='picking_types_by_company', ctx=Load()),
                                                    slice=Subscript(
                                                        value=Name(id='values', ctx=Load()),
                                                        slice=Constant(value='company_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=Name(id='res', ctx=Load()),
                                op=Add(),
                                right=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='picking_type_id', kind=None),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='populate', ctx=Load()),
                                                        attr='compute',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='get_picking_type_id', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
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
